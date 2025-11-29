#
# Conditional build:
%bcond_with	tests		# build with tests
%define		kdeappsver	25.08.3
%define		qtver		5.15.2
%define		kaname		ark
Summary:	Ark
Name:		ka6-%{kaname}
Version:	25.08.3
Release:	2
License:	GPL v2+/LGPL v2.1+
Group:		X11/Libraries
Source0:	https://download.kde.org/stable/release-service/%{kdeappsver}/src/%{kaname}-%{version}.tar.xz
# Source0-md5:	b953aaf3966fe71a2720f89a70abf285
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
Requires(post,postun):	desktop-file-utils
BuildRequires:	zlib-devel
Suggests:	lrzip
Suggests:	lzop
Suggests:	rar
Suggests:	unrar
Suggests:	zstd
%requires_eq_to Qt6Core Qt6Core-devel
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

%post
/sbin/ldconfig
%update_desktop_database_post

%postun
/sbin/ldconfig
%update_desktop_database_postun

%files -f %{kaname}.lang
%defattr(644,root,root,755)
/etc/xdg/arkrc
%attr(755,root,root) %{_bindir}/ark
%ghost %{_libdir}/libkerfuffle.so.2?
%{_libdir}/libkerfuffle.so.*.*
%dir %{_libdir}/qt6/plugins/kerfuffle
%{_libdir}/qt6/plugins/kerfuffle/kerfuffle_cli7z.so
%{_libdir}/qt6/plugins/kerfuffle/kerfuffle_cliarj.so
%{_libdir}/qt6/plugins/kerfuffle/kerfuffle_clirar.so
%{_libdir}/qt6/plugins/kerfuffle/kerfuffle_cliunarchiver.so
%{_libdir}/qt6/plugins/kerfuffle/kerfuffle_clizip.so
%{_libdir}/qt6/plugins/kerfuffle/kerfuffle_libarchive.so
%{_libdir}/qt6/plugins/kerfuffle/kerfuffle_libarchive_readonly.so
%{_libdir}/qt6/plugins/kerfuffle/kerfuffle_libzip.so
%{_libdir}/qt6/plugins/kf6/kfileitemaction/compressfileitemaction.so
%{_libdir}/qt6/plugins/kf6/kfileitemaction/extractfileitemaction.so
%dir %{_libdir}/qt6/plugins/kf6/kio_dnd
%{_libdir}/qt6/plugins/kf6/kio_dnd/extracthere.so
%{_libdir}/qt6/plugins/kf6/parts/arkpart.so
%{_desktopdir}/org.kde.ark.desktop
%{_datadir}/config.kcfg/ark.kcfg
%{_iconsdir}/hicolor/128x128/apps/ark.png
%{_iconsdir}/hicolor/48x48/apps/ark.png
%{_iconsdir}/hicolor/64x64/apps/ark.png
%{_iconsdir}/hicolor/scalable/apps/ark.svgz
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
