%define upstream_name  	    ExtUtils-Config
%define upstream_version 0.007

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	1
Summary:	A wrapper for perl's configuration
License:	GPL or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source:		http://www.cpan.org/modules/by-module/ExtUtils/%{upstream_name}-%{upstream_version}.tar.gz
BuildRequires:	perl(File::Basename)
BuildRequires:	perl(File::Spec)
BuildRequires:	perl(Test)
BuildRequires:	perl(Text::ParseWords)
BuildRequires:	perl-devel
BuildArch:	noarch

%description
A wrapper for perl's configuration.

%prep
%setup -q -n %{upstream_name}-%{upstream_version} 

%build
%__perl Makefile.PL INSTALLDIRS=vendor
make

%check
make test

%install
%makeinstall_std

%files 
%doc Changes
%{perl_vendorlib}/ExtUtils
%{_mandir}/man3/*
