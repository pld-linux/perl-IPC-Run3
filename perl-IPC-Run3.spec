#
# Conditional build:
%bcond_with	tests	# perform "make test" (one test fails)
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	IPC
%define		pnam	Run3
Summary:	IPC::Run3 - Run a subprocess in batch mode (a la system) on Unix, Win32, etc.
Summary(pl.UTF-8):	IPC::Run3 - uruchamianie podprocesu w trybie wsadowym (tak jak system)
Name:		perl-IPC-Run3
Version:	0.044
Release:	1
License:	BSD, GPL or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/IPC/RJBS/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	7df73a65d9efc7b9e7eb04075ff1fd8f
URL:		http://search.cpan.org/dist/IPC-Run3/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Test-Simple >= 0.31
BuildRequires:	perl-Time-HiRes
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Run a subprocess in batch mode (a la system) on Unix, Win32, etc.

%description -l pl.UTF-8
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
%doc Changes LICENSE README
%{perl_vendorlib}/IPC/Run3.pm
%{perl_vendorlib}/IPC/Run3
%{_mandir}/man3/IPC::Run3*.3pm*
