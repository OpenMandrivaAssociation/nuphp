%define name    nuphp
%define version 0.1.2

Name:           %{name}
Version:        %{version}
Release:        %mkrel 3
License: 	GPLv3
Summary: nuphp is a PHP4 and PHP5 library used by Nuface2 and other projects
URL: https://software.inl.fr/trac/wiki/nuphp
Source: http://software.inl.fr/releases/Nuphp/%{name}-%{version}.tar.bz2
Group: System/Servers
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Requires: webserver, php
Provides: pear(nuphp/http.php), pear(nuphp/i18n.php), pear(nuphp/debug.php), pear(nuphp/debug_php5.php), pear(nuphp/session.php)

%description
nuphp is a PHP4 and PHP5 library used by Nuface2 and other projects.

%prep
%setup -q

%build

%install
%{__rm} -rf $RPM_BUILD_ROOT
%{__mkdir} -p %{buildroot}/usr/share/%{name}
%{__cp} -av nuphp %{buildroot}/usr/share/%{name}

%clean
%{__rm} -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc AUTHORS Changelog COPYING README
/usr/share/%{name}

%post
echo "Please add: '/usr/share/nuphp' to your php include path"
