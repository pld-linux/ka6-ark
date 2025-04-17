#
# Conditional build:
%bcond_with	tests		# build with tests
%define		kdeappsver	25.04.0
%define		qtver		5.15.2
%define		kaname		ark
Summary:	Ark
Name:		ka6-%{kaname}
Version:	25.04.0
Release:	1
License:	GPL v2+/LGPL v2.1+
Group:		X11/Libraries
Source0:	https://download.kde.org/stable/release-service/%{kdeappsver}/src/%{kaname}-%{version}.tar.xz
# Source0-md5:	a8dd7fbb74f28360fc521d62a60db0cc
Patch0:		no-programs.patch
URL:		http://www.kde.org/
BuildRequires:	Qt6Concurrent-devel
BuildRequires:	Qt6Core-devel >= %{qtver}
BuildRequires:	Qt6Gui-devel
BuildRequires:	Qt6Widgets-devel
BuildRequires:	bzip2-devel
BuildRequires:	cmake >= 3.20
BuildRequires:	gettext-devel
BuildRequires:	kf6-extra-cmake-modules >= 5.53.0
BuildRequires:	kf6-karchive-devel >= 5.38.0
BuildRequires:	kf6-kconfig-devel >= 5.38.0
BuildRequires:	kf6-kcrash-devel >= 5.38.0
BuildRequires:	kf6-kdbusaddons-devel >= 5.38.0
BuildRequires:	kf6-kdoctools-devel >= 5.38.0
BuildRequires:	kf6-ki18n-devel >= 5.38.0
BuildRequires:	kf6-kiconthemes-devel >= 5.38.0
BuildRequires:	kf6-kio-devel >= 5.38.0
BuildRequires:	kf6-kitemmodels-devel >= 5.38.0
BuildRequires:	kf6-kparts-devel >= 5.38.0
BuildRequires:	kf6-kpty-devel >= 5.38.0
BuildRequires:	kf6-kservice-devel >= 5.38.0
BuildRequires:	kf6-kwidgetsaddons-devel >= 5.38.0
BuildRequires:	libarchive-devel >= 3.2.0
BuildRequires:	libzip-devel
BuildRequires:	ninja
BuildRequires:	qt6-build >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	shared-mime-info
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz-devel
BuildRequires:	zlib-devel
Suggests:	lrzip
Suggests:	lzop
Suggests:	rar
Suggests:	unrar
Suggests:	zstd
Obsoletes:	ka5-%{kaname} < %{version}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Ark is a graphical file compression/decompression utility with support
for multiple formats, including tar, gzip, bzip2, rar and zip, as well
as CD-ROM images. Ark can be used to browse, extract, create, and
modify archives.

%description -l pl.UTF-8
Ark jest graficznym programem użytkowym do kompresji/dekompresji
plików w wielu formatach, np. tar, gzip, bzip2, rar i zip, jak i
obrazów CD-ROMów. Ark może być wykorzystywany do przeglądania,
rozpakowywania, tworzenia i modyfikowania archiwów.

%prep
%setup -q -n %{kaname}-%{version}
%patch -P0 -p1

%build
%cmake \
	-B build \
	-G Ninja \
	%{!?with_tests:-DBUILD_TESTING=OFF} \
	-DKDE_INSTALL_DOCBUNDLEDIR=%{_kdedocdir} \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON
%ninja_build -C build

%if %{with tests}
ctest --test-dir build
%endif


%install
rm -rf $RPM_BUILD_ROOT
%ninja_install -C build

rm -rf $RPM_BUILD_ROOT%{_kdedocdir}/sr
rm -rf $RPM_BUILD_ROOT%{_localedir}/ie
%find_lang %{kaname} --all-name --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f %{kaname}.lang
%defattr(644,root,root,755)
/etc/xdg/arkrc
%attr(755,root,root) %{_bindir}/ark
%ghost %{_libdir}/libkerfuffle.so.2?
%attr(755,root,root) %{_libdir}/libkerfuffle.so.*.*
%dir %{_libdir}/qt6/plugins/kerfuffle
%attr(755,root,root) %{_libdir}/qt6/plugins/kerfuffle/kerfuffle_cli7z.so
%attr(755,root,root) %{_libdir}/qt6/plugins/kerfuffle/kerfuffle_cliarj.so
%attr(755,root,root) %{_libdir}/qt6/plugins/kerfuffle/kerfuffle_clirar.so
%attr(755,root,root) %{_libdir}/qt6/plugins/kerfuffle/kerfuffle_cliunarchiver.so
%attr(755,root,root) %{_libdir}/qt6/plugins/kerfuffle/kerfuffle_clizip.so
%attr(755,root,root) %{_libdir}/qt6/plugins/kerfuffle/kerfuffle_libarchive.so
%attr(755,root,root) %{_libdir}/qt6/plugins/kerfuffle/kerfuffle_libarchive_readonly.so
%attr(755,root,root) %{_libdir}/qt6/plugins/kerfuffle/kerfuffle_libzip.so
%attr(755,root,root) %{_libdir}/qt6/plugins/kf6/kfileitemaction/compressfileitemaction.so
%attr(755,root,root) %{_libdir}/qt6/plugins/kf6/kfileitemaction/extractfileitemaction.so
%dir %{_libdir}/qt6/plugins/kf6/kio_dnd
%attr(755,root,root) %{_libdir}/qt6/plugins/kf6/kio_dnd/extracthere.so
%attr(755,root,root) %{_libdir}/qt6/plugins/kf6/parts/arkpart.so
%{_desktopdir}/org.kde.ark.desktop
%{_datadir}/config.kcfg/ark.kcfg
%{_iconsdir}/hicolor/128x128/apps/ark.png
%{_iconsdir}/hicolor/48x48/apps/ark.png
%{_iconsdir}/hicolor/64x64/apps/ark.png
%{_iconsdir}/hicolor/scalable/apps/ark.svgz
%{_datadir}/kconf_update/ark.upd
%{_datadir}/kconf_update/ark_add_hamburgermenu_to_toolbar.sh
%{_mandir}/ca/man1/ark.1*
%{_mandir}/es/man1/ark.1*
%{_mandir}/fr/man1/ark.1*
%{_mandir}/gl/man1/ark.1*
%{_mandir}/it/man1/ark.1*
%{_mandir}/man1/ark.1*
%{_mandir}/nl/man1/ark.1*
%{_mandir}/pt_BR/man1/ark.1*
%{_mandir}/sl/man1/ark.1*
%{_mandir}/sr/man1/ark.1*
%{_mandir}/sr@latin/man1/ark.1*
%{_mandir}/sv/man1/ark.1*
%{_mandir}/tr/man1/ark.1*
%{_mandir}/uk/man1/ark.1*
%{_datadir}/metainfo/org.kde.ark.appdata.xml
%{_datadir}/qlogging-categories6/ark.categories
