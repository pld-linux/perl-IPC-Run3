#
# Conditional build:
%bcond_with	tests	# perform "make test" (one test fails)
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	IPC
%define		pnam	Run3
Summary:	IPC::Run3 - Run a subprocess in batch mode (a la system) on Unix, Win32, etc.
Summary(pl):	IPC::Run3 - uruchamianie podprocesu w trybie wsadowym (tak jak system)
Name:		perl-IPC-Run3
Version:	0.01
Release:	1
License:	GPL or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	d518846b8fdd1ec7188f384e9bb900e3
BuildRequires:	perl-IO-Tty >= 1.00
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautoreq	'perl(IO::Pty)'

%description
Run a subprocess in batch mode (a la system) on Unix, Win32, etc..

%description -l pl
Uruchamianie podprocesu w trybie wsadowym (tak jak system) na
Uniksach, Win32 itd.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

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
%{perl_vendorlib}/IPC/Run3.pm
%dir %{perl_vendorlib}/IPC/Run3
%{perl_vendorlib}/IPC/Run3/*
%{_mandir}/man3/*
