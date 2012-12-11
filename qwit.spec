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




%changelog
* Mon Oct 26 2009 Juan Luis Baptiste <juancho@mandriva.org> 1:0.10-1mdv2010.0
+ Revision: 459320
- Updated to 0.10 to fix bug #54890. Also removed Patch0 as it is no longer needed.

* Fri Jul 03 2009 Helio Chissini de Castro <helio@mandriva.com> 1:0.9-1mdv2010.0
+ Revision: 391932
- New upstream version

* Tue Jun 30 2009 Helio Chissini de Castro <helio@mandriva.com> r154-3mdv2010.0
+ Revision: 391073
- imported package qwit


