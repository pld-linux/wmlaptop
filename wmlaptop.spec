Summary:	Dockapp for laptop users
Summary(pl):	Aplet dla u¿ytkowników laptopów
Name:		wmlaptop
Version:	1.0
Release:	1
License:	GPL v2
Group:		X11/Window Managers/Tools
Source0:	http://www.dockapps.org/download.php/id/409/%{name}-%{version}.tar.gz
# Source0-md5:	b6fb40263b5e512edf297a8b4afd7eb4
Source1:	%{name}.desktop
URL:		http://www.dockapps.org/file.php/id/227
BuildRequires:	XFree86-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
wmlaptop is a WindowMaker dockapp that includes all that a linux user
with a laptop needs:
- Battery estimated time remaining
- Multi Batteries support
- Battery remaining charge (visual and percent)
- Auto-Frequency Scaling
- Manual Frequency Scaling
- 0-100 Cpu Load indicator
- APM and ACPI support
- sysfs and /proc filesystems support
- Kernel 2.6 series fully compatible


%description -l pl
wmlaptop jest apletem dla WindowMakera, który zawiera wszystko czego
potrzebuje u¿ytkownik laptopów:
- Szacunkowy czas do wyczerpania siê baterii
- Wsparcie dla kilku baterii
- Poziom na³adowania baterii (wizualny i procentowy)
- Automatyczne skalowanie czêstotliwo¶ci pracy procesora
- Rêczne skalowanie czêstotliwo¶ci pracy procesora
- Wska¼nik 0-100 dla obci±¿enia procesora
- Wsparcie dla sysfs i /proc
- Pe³na kompatybilno¶æ z j±drami 2.6

%prep
%setup -q

%build
%{__make} \
	CFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_applnkdir}/DockApplets}

install src/wmlaptop $RPM_BUILD_ROOT%{_bindir}
install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/DockApplets

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS README THANKS
%attr(755,root,root) %{_bindir}/*
%{_applnkdir}/DockApplets/*
