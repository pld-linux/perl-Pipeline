#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%define	pdir	Pipeline
Summary:	Pipeline - generic pipeline interface
Summary(pl.UTF-8):	Pipeline - interfejs do obsługi potoków
Name:		perl-%{pdir}
Version:	3.12
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-authors/id/R/RC/RCLAMP/%{pdir}-%{version}.tar.gz
# Source0-md5:	52cbc818aa18f7307dc00624741e5a73
URL:		http://search.cpan.org/dist/Pipeline/
BuildRequires:	perl-Class-ISA >= 0.01
BuildRequires:	perl-Data-Structure-Util >= 0.04
BuildRequires:	perl-Data-UUID >= 0.01
BuildRequires:	perl-Error >= 0.15
BuildRequires:	perl-IO-Null >= 0.01
BuildRequires:	perl-IO-String >= 0.01
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Pipelines are a mechanism to process data. They are designed to be
plugged together to make fairly complex operations act in a fairly
straightforward manner, cleanly, and simply.

%description -l pl.UTF-8
Moduł Perla Pipelines stanowi mechanizm do przetwarzania danych.
Został on zaprojektowany do włączania go w skomplikowane operacje,
żeby działały one w sposób łatwy, jasny i prosty.

%prep
%setup -q -n %{pdir}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor

%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES README
%{perl_vendorlib}/Pipeline
%{perl_vendorlib}/Pipeline.pm
%{_mandir}/man3/*
