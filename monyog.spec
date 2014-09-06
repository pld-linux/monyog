# TODO
# - pldize initscript
Summary:	MONyog MySQL Monitoring Tool
Name:		monyog
Version:	6.1.0
Release:	0.1
License:	Webyog Inc.
Group:		Applications/Databases
Source0:	https://static.webyog.com/downloads/MONyog-%{version}-0.i386.tar.gz
# NoSource0-md5:	adadfca45532b163d4f1f24f9cdff9c0
NoSource:	0
Source1:	https://static.webyog.com/downloads/MONyog-%{version}-0.x86_64.tar.gz
# NoSource1-md5:	4cc3950bca955474b73baa57c4c4d9d7
NoSource:	1
URL:		https://www.webyog.com/product/monyog
ExclusiveArch:	%{ix86} %{x8664}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_appdir	%{_datadir}/%{name}

%description
MONyog is a monitoring and advisory tool for MySQL Community, MySQL
Enterprise and MariaDB.

MONyog helps MySQL Database Administrators to manage more servers,
tune their MySQL servers and fix problems with MySQL database
applications. MONyog is agent-less, and does not require anything to
be installed on the MySQL servers. MONyog helps monitor enterprise
database environments and provides expert advice on how even those new
to MySQL can tighten security, optimize performance and reduce
downtime of their MySQL powered systems.

%prep
%ifarch %{ix86}
%setup -qcT -a0
%endif
%ifarch %{x8664}
%setup -qcT -a1
%endif

mv MONyog/* .

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sbindir},%{_appdir},/etc/{rc.d/init.d,logrotate.d}}
cp -a MONyog.lua MONyog.mib res $RPM_BUILD_ROOT%{_appdir}
install -p bin/MONyog $RPM_BUILD_ROOT/etc/rc.d/init.d/%{name}
install -p bin/MONyog-bin $RPM_BUILD_ROOT%{_sbindir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(754,root,root) /etc/rc.d/init.d/monyog
%attr(755,root,root) %{_sbindir}/monyog
%{_appdir}