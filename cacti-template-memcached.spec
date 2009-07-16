%define		plugin memcached
Summary:	Memcached Cacti Template
Name:		cacti-plugin-%{plugin}
Version:	1.0
Release:	3
License:	GPL v2
Group:		Applications/WWW
Source0:	http://content.dealnews.com/dealnews/developers/cacti-%{plugin}-%{version}.tar.gz
# Source0-md5:	1febadae299aff606860da60ef3bd80e
URL:		http://dealnews.com/developers/cacti/memcached.html
Patch0:		shebang.patch
Requires:	cacti >= 0.8.6j
Requires:	cacti-add_template
Requires:	python-memcached
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		cactidir		/usr/share/cacti
%define		resourcedir		%{cactidir}/resource
%define		scriptsdir		%{cactidir}/scripts

%description
This template provides a host template and associated graphs for
graphing the output of the memcached stats command on individual
memcached installations.

Graphs are provided for Bytes Used with total capacity, Cache Hits and
Misses per second, Current Connections, Items Cached, Inbound and
Outbound Network Traffic (bits per second), and Requests per Second
for both the get and set commands.

%prep
%setup -q -n cacti-%{plugin}-%{version}
%patch0 -p1

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{resourcedir},%{scriptsdir}}
cp -a *.xml $RPM_BUILD_ROOT%{resourcedir}
install *.py $RPM_BUILD_ROOT%{scriptsdir}

%post
%{_sbindir}/cacti-add_template %{resourcedir}/cacti_memcached_host_template.xml

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{scriptsdir}/memcached.py
%{resourcedir}/cacti_memcached_host_template.xml
