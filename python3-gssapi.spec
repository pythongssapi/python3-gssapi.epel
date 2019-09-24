# NOTE: tests are disabled since should_be has not yet been packaged.
# To re-enable, uncomment the 'check' section and lines marked 'for tests'
%global run_tests 0

%global mname python-gssapi
%global python3 python%{python3_pkgversion}

Name:           python3-gssapi
Version:        1.3.0
Release:        3%{?dist}
Summary:        Python 3 Bindings for GSSAPI (RFC 2743/2744 and extensions)

License:        ISC
URL:            https://github.com/pythongssapi/%{mname}
Source0:        https://github.com/pythongssapi/%{mname}/releases/download/v%{version}/%{mname}-%{version}.tar.gz

# Patches

Requires:       %{python3}-six
Requires:       %{python3}-decorator

BuildRequires:  krb5-devel >= 1.10
BuildRequires:  krb5-libs >= 1.10
BuildRequires:  %{python3}-devel
BuildRequires:  %{python3}-setuptools
BuildRequires:  %{python3}-Cython

%if 0%{?run_tests}
BuildRequires:  krb5-server >= 1.10
BuildRequires:  %{python3}-nose
BuildRequires:  %{python3}-nose-parameterized
BuildRequires:  %{python3}-should-be
%endif

%global _description\
A set of Python 3 bindings to the GSSAPI C library providing both\
a high-level pythonic interfaces and a low-level interfaces\
which more closely matches RFC 2743.  Includes support for\
RFC 2743, as well as multiple extensions.

%description %_description


%prep
%setup -q -n %{mname}-%{version}


%build
%py3_build


%install
%py3_install


%check
%if 0%{?run_tests}
%{__python3} setup.py nosetests
%endif


%files
%doc README.txt LICENSE.txt
%{python3_sitearch}/gssapi
%{python3_sitearch}/gssapi-%{version}-py%{python3_version}.egg-info


%changelog
* Tue Sep 24 2019 Robbie Harwood <Mrharwood@redhat.com> - 1.3.0-3
- More of the same
- Resolves: #1755043

* Tue Sep 24 2019 Robbie Harwood <Mrharwood@redhat.com> - 1.3.0-2
- Try again at making the specfile work
- Resolves: #1755043

* Thu Jan 10 2017 Robbie Harwood <rharwood@redhat.com> - 1.3.0-1
- Minor changes to el7 to enable building on el6
