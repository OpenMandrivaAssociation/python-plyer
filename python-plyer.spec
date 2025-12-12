%define module plyer

Summary:	A platform-independent Python wrapper for platform-dependent APIs
Name:		python-%{module}
Version:	2.1.0
Release:	3
License:	Expat
Url:		https://plyer.readthedocs.io
Group:		Development/Languages/Python
Source:		https://files.pythonhosted.org/packages/source/p/%{module}/%{module}-%{version}.tar.gz

BuildRequires:	pkgconfig(python3)
#BuildRequires:	python3dist(mock)
BuildRequires:	python3dist(pytest)
BuildRequires:	python3dist(setuptools)

BuildArch:	noarch

%description
Plyer is a Python library for accessing features of your hardware / platforms.

Plyer tries not to reinvent the wheel, and will call for external libraries 
to implement the api in the easiest way, depending on the current platform.

%files
%doc README.md
%{python_sitelib}/*

#----------------------------------------------------------------------------

%prep
%autosetup -n %{module}-%{version}

%build
%py_build

%install
%py_install

