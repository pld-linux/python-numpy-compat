%define		module	numpy
%define		mname	Numeric

Summary:	Python numerical facilities
Summary(pl):	Modu�y do oblicze� numerycznych dla j�zyka Python
Name:		python-%{module}
Version:	24.2
Release:	1
License:	distributable
Group:		Libraries/Python
Source0:	http://dl.sourceforge.net/numpy/%{mname}-%{version}.tar.gz
# Source0-md5:	2ae672656e06716a149acb048cca3093
URL:		http://sourceforge.net/projects/numpy/
BuildRequires:	python-devel >= 1:2.3
%pyrequires_eq	python-libs
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
NumPy is a collection of extension modules to provide high-performance
multidimensional numeric arrays to the Python programming language.

%description -l pl
Pakiet umo�liwia wydajne obliczenia numeryczne na macierzach
wielowymiarowych.

%package devel
Summary:	C header files for numerical modules
Summary(pl):	Pliki nag��wkowe j�zyka C modu��w numerycznych
Group:		Development/Languages/Python
%pyrequires_eq	python-devel
Requires:	%{name} = %{version}-%{release}

%description devel
C header files for numerical modules.

%description devel -l pl
Pliki nag��wkowe j�zyka C modu��w numerycznych.

%package FFT
Summary:	Interface to the FFTPACK FORTRAN library
Summary(pl):	Interfejs do biblioteki FFTPACK j�zyka Fortran
Group:		Libraries/Python
%pyrequires_eq	python-libs
Requires:	%{name} = %{version}-%{release}

%description FFT
The FFT.py module provides a simple interface to the FFTPACK FORTRAN
library, which is a powerful standard library for doing fast Fourier
transforms of real and complex data sets.

%description FFT -l pl
Modu� FFT zawiera prosty interfejs do biblioteki FFTPACK j�zyka
Fortran. Ta biblioteka o wysokich mo�liwo�ciach jest standardowo
u�ywana do prowadzenia oblicze� za pomoc� dyskretnej transformaty
Fouriera na liczba rzeczywistych i zespolonych.

# -- will be released as separate package
#%package kinds
#Summary:	Implementation of PEP 0242 - precision and range control of numeric computations
#Summary(pl):	Implementacja propozycji PEP 0242 - mo�liwo�� kontrolowania precyzji i zakresu oblicze� numerycznych
#Group:		Libraries/Python
#%pyrequires_eq	python-libs
#Requires:	%{name} = %{version}-%{release}
#
#%description kinds
#This is implementation of PEP 0242. PEP's abstract follows:
#
#This proposal gives the user optional control over the precision and
#range of numeric computations so that a computation can be written
#once and run anywhere with at least the desired precision and range.
#It is backward compatible with existing code.
#
#%description kinds -l pl
#Modu� zawiera implementacj� propozycji PEP 0242. Oto jej streszczenie.
#
#Propozycja ta umo�liwia u�ytkownikowi, opcjonalnie, kontrol� nad
#precyzj� i zakresem oblicze� numerycznych. Dzi�ki temu raz napisane
#obliczenia mog� by� uruchamiane na dowolnej maszynie. Mechanizm jest
#kompatybilny wstecz z istniej�cymi programami.

%package MA
Summary:	MA - a facility for dealing with masked arrays
Summary(pl):	Modu� do obs�ugi macierzy niepe�nych
Group:		Libraries/Python
%pyrequires_eq	python-libs
Requires:	%{name} = %{version}-%{release}

%description MA
Masked arrays are arrays that may have missing or invalid entries.
Module MA provides a work-alike replacement for Numeric that supports
data arrays with masks.

%description MA -l pl
Macierze niepe�ne s� to macierze, kt�rym mo�e brakowa� lub mog�
zawiera� niepoprawne warto�ci. Modu� MA zawiera odpowiednie narz�dzia
do operowania na tego typu macierzach.

# -- removed(?)
#%package Properties
#Summary:	Property class implementation for Python
#Summary(pl):	Implementacja klasy z w�a�ciwo�ciami dla j�zyka Python
#Group:		Libraries/Python
#%pyrequires_eq	python-libs
#Requires:	%{name} = %{version}-%{release}
#
#%description Properties
#PropertiedClass is a mixin class that can be used to emulate
#properties in a Python class. A property is an attribute whose read,
#write, or deleting requires special handling. It is also possible to
#use this facility to prevent the writing or deleting of a property.
#
#%description Properties -l pl
#PropertiedClass jest klas�, kt�ra mo�e by� u�yta do emulacji
#w�a�ciwo�ci w klasach j�zyka Python. W�a�ciwo�� klasy jest atrybutem,
#kt�rego czytanie, przypisywanie mu warto�ci, czy te� jego usuwanie
#powinno by� traktowane w spos�b specjalny. Mechanizm ten mo�e by� te�
#u�ywany w celu ustalenia jakiego� atrybutu jako tylko do odczytu.

%package RNG
Summary:	Random Number Generator Object for NumPy
Summary(pl):	Obiekt generatora liczb losowych dla modu�u NumPy
Group:		Libraries/Python
%pyrequires_eq	python-libs
Requires:	%{name} = %{version}-%{release}

%description RNG
RNG provides a random number object to Numerical Python.

%description RNG -l pl
Modu� ten zawiera implementacj� obiektu generatora liczb losowych dla
j�zyka Python.

%prep
%setup -q -n %{mname}-%{version}

%build
CC="%{__cc}"; export CC
CFLAGS="%{rpmcflags}"; export CFLAGS
python setup.py build

%install
rm -rf $RPM_BUILD_ROOT

python setup.py install \
	--root=$RPM_BUILD_ROOT

%py_ocomp $RPM_BUILD_ROOT%{py_sitedir}
%py_comp $RPM_BUILD_ROOT%{py_sitedir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{py_sitedir}/%{mname}.pth
%dir %{py_sitedir}/%{mname}
%attr(755,root,root) %{py_sitedir}/%{mname}/*.so
%dir %{py_sitedir}/%{mname}/Numeric_headers
%{py_sitedir}/%{mname}/Numeric_headers/__init__.*
%{py_sitedir}/%{mname}/*.py[co]
%{py_sitedir}/%{mname}/*.py

%files devel
%defattr(644,root,root,755)
%{py_incdir}/%{mname}

%files FFT
%defattr(644,root,root,755)
%dir %{py_sitedir}/%{mname}/FFT
%attr(755,root,root) %{py_sitedir}/%{mname}/FFT/*.so
%{py_sitedir}/%{mname}/FFT/*.py[co]
%{py_sitedir}/%{mname}/FFT/*.py

#%files kinds
#%defattr(644,root,root,755)
#%dir %{py_sitedir}/%{mname}/kinds
#%attr(755,root,root) %{py_sitedir}/%{mname}/kinds/*.so
#%{py_sitedir}/%{mname}/kinds/*.py[co]

%files MA
%defattr(644,root,root,755)
%dir %{py_sitedir}/%{mname}/MA
%{py_sitedir}/%{mname}/MA/*.py[co]
%{py_sitedir}/%{mname}/MA/*.py

#%files Properties
#%defattr(644,root,root,755)
#%dir %{py_sitedir}/%{mname}/PropertiedClasses
#%{py_sitedir}/%{mname}/PropertiedClasses/*.py[co]

%files RNG
%defattr(644,root,root,755)
%dir %{py_sitedir}/%{mname}/RNG
%attr(755,root,root) %{py_sitedir}/%{mname}/RNG/*.so
%{py_sitedir}/%{mname}/RNG/*.py[co]
%{py_sitedir}/%{mname}/RNG/*.py