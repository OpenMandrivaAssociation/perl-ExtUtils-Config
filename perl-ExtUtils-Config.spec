%define module ExtUtils-Config
%undefine _debugsource_packages

Name:		perl-%{module}
Version:	0.008
Release:	1
Summary:	ExtUtils::Config - A wrapper for perl's configuration
URL:		https://metacpan.org/pod/ExtUtils::Config
Source:		https://cpan.org/modules/by-module/ExtUtils/%{module}-%{version}.tar.gz
License:	Perl (Artistic or GPL)
Group:		Development/Perl
BuildRequires:	perl
BuildRequires:	perl(ExtUtils::MakeMaker)
BuildArch:	noarch
# For tests only
BuildRequires:	perl(Test::More)

%description
ExtUtils::Config is an abstraction around the %Config hash. By itself it is not
a particularly interesting module by any measure, however it ties together a
family of modern toolchain modules.

%prep
%autosetup -p1 -n %{module}-%{version}
perl Makefile.PL INSTALLDIRS=vendor

%build
%make_build

%check
make test

%install
%make_install INSTALLDIRS=vendor

%files
%doc Changes MANIFEST README
%{perl_vendorlib}/*/*
%{_mandir}/man3/*.3pm*
