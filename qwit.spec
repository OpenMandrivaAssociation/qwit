Name: qwit
Version: 0.10
Release: %mkrel 1
Epoch: 1
URL: http://code.google.com/p/qwit/
Summary: Qwit is a simple Qt4-based client for Twitter
License: GPLv3+
Group: Networking/Instant messaging
Source0: http://qwit.googlecode.com/files/%{name}-%{version}-src.tar.bz2
#Patch0: qwit-r154-cmakefile.patch 
BuildRequires: qt4-devel
BuildRequires: cmake
BuildRequires: automoc4
BuildRoot: %{_tmppath}/{%name}-buildroot

%description
This is a crossplatform twitter client writen in Qt4, it depends only on Qt4

%files
%defattr(-,root,root)
%doc AUTHORS INSTALL README
%_datadir/applications/qwit.desktop
%_iconsdir/qwit.png
%qt4bin/qwit
%qt4dir/translations/*

#-------------------------------------------------------------------

%prep
%setup -q -n %{name}-%{version}-src
#%patch0  -p1 


%build
%cmake_qt4
%make

%install
rm -rf %{buildroot}
%makeinstall_std -C build

%clean
rm -rf %{buildroot}


