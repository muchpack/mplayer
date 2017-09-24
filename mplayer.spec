%global debug_package %{nil}

%define         codecdir %{_libdir}/codecs
%define         faad2min 1:2.6.1

Name:           mplayer
Version:        1.3.0
Release:        12%{?dist}
Summary:        Movie player playing most video formats and DVDs
License:        GPLv2+ or GPLv3+
URL:            http://www.mplayerhq.hu/
Source0:        http://www.mplayerhq.hu/MPlayer/releases/MPlayer-%{version}.tar.xz
Source1:        http://www.mplayerhq.hu/MPlayer/skins/Blue-1.11.tar.bz2
# set defaults for Fedora
Patch1:         mplayer-config.patch
# use system FFmpeg libraries and use roff include statements instead of symlinks
Patch:          mplayer-ffmpeg.patch
# Include Samba
Patch2:         include-samba-4.0.patch

BuildRequires:  SDL-devel
BuildRequires:  a52dec-devel
BuildRequires:  aalib-devel
BuildRequires:  bzip2-devel
BuildRequires:  alsa-lib-devel
BuildRequires:  desktop-file-utils
BuildRequires:  enca-devel
BuildRequires:  faad2-devel >= %{faad2min}
BuildRequires:  ffmpeg-devel >= 0.10
BuildRequires:  fontconfig-devel
BuildRequires:  freetype-devel >= 2.0.9
BuildRequires:  fribidi-devel
BuildRequires:  giflib-devel
BuildRequires:  gsm-devel
BuildRequires:  gtk2-devel
BuildRequires:  ladspa-devel
BuildRequires:  lame-devel
BuildRequires:  libGL-devel
BuildRequires:  libXinerama-devel
BuildRequires:  libXScrnSaver-devel
BuildRequires:  libXv-devel
BuildRequires:  libXvMC-devel
BuildRequires:  libXxf86vm-devel
BuildRequires:  libass-devel >= 0.9.10
BuildRequires:  libbluray-devel
BuildRequires:  libbs2b-devel
BuildRequires:  libcaca-devel
BuildRequires:  libcdio-paranoia-devel
BuildRequires:  libdca-devel
BuildRequires:  libdv-devel
BuildRequires:  libdvdnav-devel >= 4.1.3-1
BuildRequires:  libjpeg-devel
BuildRequires:  libmpeg2-devel
BuildRequires:  mpg123-devel
BuildRequires:  librtmp-devel
BuildRequires:  libtheora-devel
BuildRequires:  libvdpau-devel
BuildRequires:  libvorbis-devel
BuildRequires:  lirc-devel
BuildRequires:  lzo-devel >= 2
BuildRequires:  pulseaudio-libs-devel
BuildRequires:  speex-devel >= 1.1
BuildRequires:  twolame-devel
BuildRequires:  x264-devel >= 0.0.0-0.28
BuildRequires:  xvidcore-devel >= 0.9.2
BuildRequires:  yasm


# BuildRequires: arts-devel
BuildRequires: libXxf86dga-devel
# BuildRequires: directfb-devel
#BuildRequires: esound-devel
BuildRequires:  faac-devel
BuildRequires: jack-audio-connection-kit-devel
BuildRequires:  libmad-devel
# BuildRequires:  libmpcdec-devel
# BuildRequires:  libnemesi-devel >= 0.6.3
# BuildRequires: openal-soft-devel
BuildRequires: libsmbclient-devel
# BuildRequires: svgalib-devel
# BuildRequires: xmms-devel

%if 0%{?svn}
# for XML docs, SVN only
BuildRequires:  docbook-dtds
BuildRequires:  docbook-style-xsl
BuildRequires:  libxml2
BuildRequires:  libxslt
%endif
# new make requires
BuildRequires:  opencore-amr-devel
BuildRequires:  libmng-devel
BuildRequires:  schroedinger-devel
BuildRequires:  libvpx-devel
BuildRequires:  live555-devel
BuildRequires:  git
BuildRequires:  opus-devel
BuildRequires:  rtmpdump
BuildRequires:  gnutls-devel
BuildRequires:  libdvdcss-devel
BuildRequires:  libdvdread-devel
BuildRequires:  libdvdnav-devel
#
Obsoletes:      mplayer-fonts
Requires:       faad2-libs >= %{faad2min}
Requires:       mplayer-common = %{version}-%{release}

%description
MPlayer is a movie player that plays most MPEG, VOB, AVI, OGG/OGM,
VIVO, ASF/WMA/WMV, QT/MOV/MP4, FLI, RM, NuppelVideo, yuv4mpeg, FILM,
RoQ, and PVA files. You can also use it to watch VCDs, SVCDs, DVDs,
3ivx, RealMedia, and DivX movies.
It supports a wide range of output drivers including X11, XVideo, DGA,
OpenGL, SVGAlib, fbdev, AAlib, DirectFB etc. There are also nice
antialiased shaded subtitles and OSD.
The following on-default rpmbuild options are available:
--with samba:   Enable Samba (smb://) support
--with xmms:    Enable XMMS input plugin support
--without amr:  Disable AMR support
--with faac:    Enable FAAC support
--with libmad:  Enable libmad support
--with openal:  Enable OpenAL support
--with jack:    Enable JACK support
--with arts:    Enable aRts support
--with esound:  Enable EsounD support
--with dga:     Enable DGA support
--with directfb:Enable DirectFB support
--with svgalib: Enable SVGAlib support
--with nemesi:  Enable libnemesi RTSP support

%package        common
Summary:        MPlayer common files

%description    common
This package contains common files for MPlayer packages.

%package        gui
Summary:        GUI for MPlayer
Requires:       mplayer-common = %{version}-%{release}
Requires:       hicolor-icon-theme

%description    gui
This package contains a GUI for MPlayer and a default skin for it.

%package     -n mencoder
Summary:        MPlayer movie encoder
Requires:       mplayer-common = %{version}-%{release}

%description -n mencoder
This package contains the MPlayer movie encoder. 

%package        doc
Summary:        MPlayer documentation in various languages

%description    doc
MPlayer documentation in various languages.

%package        tools
Summary:        Useful scripts for MPlayer
Requires:       mencoder = %{version}-%{release}
Requires:       mplayer = %{version}-%{release}

%description    tools
This package contains various scripts from MPlayer TOOLS directory.

%define mp_configure \
./configure --prefix=/usr \\\
    --libdir=%{_libdir} \\\
    --codecsdir=%{codecdir} \\\
    --datadir=%{_datadir}/mplayer \\\
    --disable-ffmpeg_a \\\
    --enable-runtime-cpudetection \\\
    --disable-arts \\\
    --disable-liblzo \\\
    --disable-speex \\\
    --disable-openal \\\
    --disable-libdv \\\
    --disable-musepack \\\
    --disable-esd \\\
    --disable-mga \\\
    --disable-ass-internal \\\
    --disable-cdparanoia \\\
    --enable-xvmc \\\
    --enable-radio \\\
    --enable-radio-capture \\\
    --enable-smb \\\
    --language=all \\\
    --confdir=/etc/mplayer \\\

%prep
%if 0%{?svn}
%setup -q -n mplayer-export-%{svnbuild}
%else
%setup -q -n MPlayer-%{version}%{?pre}
rm -rf ffmpeg
%endif

%patch -p0
%patch1 -p0
%patch2 -p1


mkdir GUI
cp -a `ls -1|grep -v GUI` GUI/

./version.sh


%build

pushd GUI
%{mp_configure}--enable-gui --disable-mencoder

%{__make} V=1 %{?_smp_mflags}
popd

%{mp_configure}--disable-gui --enable-mencoder

%{__make} V=1 %{?_smp_mflags}

%if 0%{?svn}
# build HTML documentation from XML files 
%{__make} html-chunked
%endif


%ifarch i686
sed 's|-march=i486|-march=i686|g' -i config.mak
%endif

%install

rm -rf $RPM_BUILD_ROOT doc

make install DESTDIR=$RPM_BUILD_ROOT INSTALLSTRIP=
for file in aconvert.sh divx2svcd.sh mencvcd.sh midentify.sh mpconsole.sh qepdvcd.sh subsearch.sh ; do
install -pm 755 TOOLS/$file $RPM_BUILD_ROOT%{_bindir}/`basename $file .sh`
done

for file in calcbpp.pl countquant.pl dvd2divxscript.pl ; do
install -pm 755 TOOLS/$file $RPM_BUILD_ROOT%{_bindir}/`basename $file .pl`
done

for file in vobshift.py ; do
install -pm 755 TOOLS/$file $RPM_BUILD_ROOT%{_bindir}/`basename $file .py`
done

mkdir -p $RPM_BUILD_ROOT%{_datadir}/mplayer
install -pm 644 TOOLS/*.fp $RPM_BUILD_ROOT%{_datadir}/mplayer/

# Clean up documentation
mkdir doc
cp -pR DOCS/* doc/
rm -r doc/man doc/xml doc/README
mv doc/HTML/* doc/
rm -rf doc/HTML

# Default config files
install -Dpm 644 etc/example.conf \
    $RPM_BUILD_ROOT%{_sysconfdir}/mplayer/mplayer.conf

install -dm 755 %{buildroot}/%{_sysconfdir}/mplayer/
install -m 0644 %{_builddir}/MPlayer-1.3.0/etc/*.conf %{buildroot}/%{_sysconfdir}/mplayer/

# desktop file (FS#14770)
install -Dm644 %{_builddir}/MPlayer-1.3.0/etc/mplayer.desktop %{buildroot}/usr/share/applications/mplayer.desktop
install -Dm644 %{_builddir}/MPlayer-1.3.0/etc/mplayer256x256.png %{buildroot}/usr/share/pixmaps/mplayer.png

# GUI mplayer
install -pm 755 GUI/%{name} $RPM_BUILD_ROOT%{_bindir}/gmplayer

# Default skin
install -dm 755 $RPM_BUILD_ROOT%{_datadir}/mplayer/skins
tar xjC $RPM_BUILD_ROOT%{_datadir}/mplayer/skins --exclude=.svn -f %{SOURCE1}
ln -s Blue $RPM_BUILD_ROOT%{_datadir}/mplayer/skins/default

# Icons
for iconsize in 16x16 22x22 24x24 32x32 48x48 256x256
do
install -dm 755 $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/$iconsize/apps
install -pm 644 etc/mplayer$iconsize.png \
    $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/$iconsize/apps/mplayer.png
done

# Codec dir
install -dm 755 $RPM_BUILD_ROOT%{codecdir}

%post gui
gtk-update-icon-cache -qf %{_datadir}/icons/hicolor &>/dev/null || :
update-desktop-database &>/dev/null || :


%postun gui
gtk-update-icon-cache -qf %{_datadir}/icons/hicolor &>/dev/null || :
update-desktop-database &>/dev/null || :


%files
%{_bindir}/mplayer

%files common
%doc AUTHORS Changelog Copyright LICENSE README
%dir %{_sysconfdir}/mplayer
%config(noreplace) %{_sysconfdir}/mplayer/mplayer.conf
%config(noreplace) %{_sysconfdir}/mplayer/input.conf
%config(noreplace) %{_sysconfdir}/mplayer/menu.conf
%config(noreplace) %{_sysconfdir}/mplayer/codecs.conf
%config(noreplace) %{_sysconfdir}/mplayer/dvb-menu.conf
%config(noreplace) %{_sysconfdir}/mplayer/example.conf
%dir %{codecdir}/
%dir %{_datadir}/mplayer/
%{_mandir}/man1/mplayer.1*
%lang(cs) %{_mandir}/cs/man1/mplayer.1*
%lang(de) %{_mandir}/de/man1/mplayer.1*
%lang(es) %{_mandir}/es/man1/mplayer.1*
%lang(fr) %{_mandir}/fr/man1/mplayer.1*
%lang(hu) %{_mandir}/hu/man1/mplayer.1*
%lang(it) %{_mandir}/it/man1/mplayer.1*
%lang(pl) %{_mandir}/pl/man1/mplayer.1*
%lang(ru) %{_mandir}/ru/man1/mplayer.1*
%lang(zh_CN) %{_mandir}/zh_CN/man1/mplayer.1*

%files gui
%{_bindir}/gmplayer
%{_datadir}/applications/*mplayer.desktop
%{_datadir}/icons/hicolor/*/apps/mplayer.png
%{_datadir}/mplayer/skins/
%{_datadir}/pixmaps/mplayer.png

%files -n mencoder
%{_bindir}/mencoder
%{_mandir}/man1/mencoder.1*
%lang(cs) %{_mandir}/cs/man1/mencoder.1*
%lang(de) %{_mandir}/de/man1/mencoder.1*
%lang(es) %{_mandir}/es/man1/mencoder.1*
%lang(fr) %{_mandir}/fr/man1/mencoder.1*
%lang(hu) %{_mandir}/hu/man1/mencoder.1*
%lang(it) %{_mandir}/it/man1/mencoder.1*
%lang(pl) %{_mandir}/pl/man1/mencoder.1*
%lang(ru) %{_mandir}/ru/man1/mencoder.1*
%lang(zh_CN) %{_mandir}/zh_CN/man1/mencoder.1*

%files doc
%doc doc/en/ doc/tech/
%lang(cs) %doc doc/cs/
%lang(de) %doc doc/de/
%lang(es) %doc doc/es/
%lang(fr) %doc doc/fr/
%lang(hu) %doc doc/hu/
%lang(pl) %doc doc/pl/
%lang(ru) %doc doc/ru/
%lang(zh_CN) %doc doc/zh_CN/

%files tools
%{_bindir}/aconvert
%{_bindir}/calcbpp
%{_bindir}/countquant
%{_bindir}/divx2svcd
%{_bindir}/dvd2divxscript
%{_bindir}/mencvcd
%{_bindir}/midentify
%{_bindir}/mpconsole
%{_bindir}/qepdvcd
%{_bindir}/subsearch
%{_bindir}/vobshift
%{_datadir}/mplayer/*.fp

%changelog

* Sat Sep 23 2017 Unitedrpms Project <unitedrpms AT protonmail DOT com> 1.3.0-12  
- Automatic Mass Rebuild

* Mon Sep 18 2017 Unitedrpms Project <unitedrpms AT protonmail DOT com> 1.3.0-11
- Rebuilt for mpg123

* Thu Aug 03 2017 Unitedrpms Project <unitedrpms AT protonmail DOT com> 1.3.0-9  
- Automatic Mass Rebuild

* Mon Jul 31 2017 Unitedrpms Project <unitedrpms AT protonmail DOT com> 1.3.0-8  
- Automatic Mass Rebuild

* Tue Apr 18 2017 Unitedrpms Project <unitedrpms AT protonmail DOT com> 1.3.0-7  
- Automatic Mass Rebuild

* Sat Mar 18 2017 Unitedrpms Project <unitedrpms AT protonmail DOT com> 1.3.0-6  
- Rebuilt for libbluray

* Wed Mar 15 2017 Unitedrpms Project <unitedrpms AT protonmail DOT com> 1.3.0-5  
- Automatic Mass Rebuild

* Thu Jul 07 2016 David Vásquez <davidjeremias82 AT gmail DOT com> 1.3.0-3
- Rebuilt for FFmpeg 3.1 

* Sun Jun 26 2016 The UnitedRPMs Project (Key for UnitedRPMs infrastructure) <unitedrpms@protonmail.com> - 1.3.0-2
- Rebuild with new ffmpeg

* Tue Apr 19 2016 David Vásquez <davidjeremias82 AT gmail DOT com> 1.3.0-1
- Updated to 1.3.0

* Sat Apr 02 2016 Julian Sikorski <belegdol@fedoraproject.org> - 1.2.1-2
- Fixed BuildRequires so that audio CD support actually works

* Thu Jan 28 2016 Julian Sikorski <belegdol@fedoraproject.org> - 1.2.1-1
- Updated to 1.2.1
- Removed asm.h from mplayer-ffmpeg.patch

* Thu Oct 29 2015 Julian Sikorski <belegdol@fedoraproject.org> - 1.2-1
- Updated to 1.2
- Updated Blue skin to 1.11

* Thu May 07 2015 Julian Sikorski <belegdol@fedoraproject.org> - 1.1-33.20150505svn
- 20150505 snapshot
- Updated ffmpeg patch

* Sat Jan 31 2015 Julian Sikorski <belegdol@fedoraproject.org> - 1.1-32.20150123svn
- 20150123 snapshot
- Internal libdvd* are no more, cleaned up the spec accordingly

* Tue Oct 21 2014 Julian Sikorski <belegdol@fedoraproject.org> - 1.1-31.20141020svn
- 20141020 snapshot

* Mon Oct 20 2014 Sérgio Basto <sergio@serjux.com> - 1.1-30.20140919svn
- Rebuilt for FFmpeg 2.4.3

* Wed Oct 01 2014 Sérgio Basto <sergio@serjux.com> - 1.1-29.20140919svn
- Rebuilt again for FFmpeg 2.3.x (with FFmpeg 2.3.x in buildroot)

* Sat Sep 27 2014 kwizart <kwizart@gmail.com> - 1.1-28.20140919svn
- Rebuilt for FFmpeg 2.3x

* Thu Sep 25 2014 Julian Sikorski <belegdol@fedoraproject.org> - 1.1-27.20140919svn
- 20140919 snapshot

* Wed Aug 06 2014 Julian Sikorski <belegdol@fedoraproject.org> - 1.1-26.20140806svn
- 20140806 snapshot

* Sat Jul 12 2014 Julian Sikorski <belegdol@fedoraproject.org> - 1.1-25.20140711svn
- 20140711 snapshot

* Thu Mar 27 2014 Julian Sikorski <belegdol@fedoraproject.org> - 1.1-24.20140327svn
- 20140327 snapshot

* Fri Mar 21 2014 Julian Sikorski <belegdol@fedoraproject.org> - 1.1-23.20140301svn
- Rebuilt for libass-0.10.2

* Tue Mar 18 2014 Julian Sikorski <belegdol@fedoraproject.org> - 1.1-22.20140301svn
- Rebuilt for x264

* Thu Mar 06 2014 Nicolas Chauvet <kwizart@gmail.com> - 1.1-21.20140301svn
- Rebuilt for x264

* Sat Mar 01 2014 Julian Sikorski <belegdol@fedoraproject.org> - 1.1-20.20140301svn
- 20140301 snapshot

* Tue Feb 11 2014 Julian Sikorski <belegdol@fedoraproject.org> - 1.1-19.20140211svn
- 20140211 snapshot

* Sun Jan 12 2014 Julian Sikorski <belegdol@fedoraproject.org> - 1.1-18.20140111svn
- 20140111 snapshot

* Tue Jan 07 2014 Nicolas Chauvet <kwizart@gmail.com> - 1.1-17.20131125svn
- Rebuilt for librtmp

* Thu Nov 28 2013 Julian Sikorski <belegdol@fedoraproject.org> - 1.1-16.20131125svn
- 20131125 snapshot

* Sat Nov 02 2013 Julian Sikorski <belegdol@fedoraproject.org> - 1.1-15.20131102svn
- 20131102 snapshot

* Tue Oct 22 2013 Nicolas Chauvet <kwizart@gmail.com> - 1.1-14.20130811svn
- Rebuilt for x264

* Tue Aug 13 2013 Julian Sikorski <belegdol@fedoraproject.org> - 1.1-13.20130811svn
- 20130811 snapshot

* Thu Aug 01 2013 Julian Sikorski <belegdol@fedoraproject.org> - 1.1-12.20130801svn
- 20130801 snapshot
- Updated the ffmpeg patch
- Re-numbered the patches

* Sat Jul 20 2013 Nicolas Chauvet <kwizart@gmail.com> - 1.1-11.20130416svn
- Rebuilt for x264

* Fri Jun 07 2013 Julian Sikorski <belegdol@fedoraproject.org> - 1.1-10.20130416svn

* Thu Jan  6 2005 Ville Skyttä <ville.skytta at iki.fi> 0:1.0-0.lvn.0.17.pre6a
- Update to 1.0pre6a (== 1.0pre6 + included HTML docs).
