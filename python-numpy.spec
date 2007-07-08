#
# TODO:
#	- description for oldnumeric
#
%define		module	numpy

Summary:	Python numerical facilities
Summary(pl.UTF-8):	Moduły do obliczeń numerycznych dla języka Python
Name:		python-%{module}
Version:	1.0.3
Release:	0.1
Epoch:		1
License:	distributable
Group:		Libraries/Python
Source0:	http://dl.sourceforge.net/numpy/%{module}-%{version}-2.tar.gz
# Source0-md5:	ff0ec1a633e426c8230b6c9d333cc1e6
URL:		http://sourceforge.net/projects/numpy/
BuildRequires:	python-devel >= 1:2.5
%pyrequires_eq	python-libs
# -- dropped some time ago
Obsoletes:	python-numpy-Properties
# -- dropped some time ago, should have been released as separate package, but wasn't
Obsoletes:	python-numpy-kinds
# old subpackage, merged into main
Obsoletes:	python-numpy-FFT
# -- dropped during Numeric->numpy transition
Obsoletes:	python-numpy-MA
Obsoletes:	python-numpy-RNG
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
NumPy is a collection of extension modules to provide high-performance
multidimensional numeric arrays to the Python programming language.

%description -l pl.UTF-8
Pakiet umożliwia wydajne obliczenia numeryczne na macierzach
wielowymiarowych.

%package devel
Summary:	C header files for numerical modules
Summary(pl.UTF-8):	Pliki nagłówkowe języka C modułów numerycznych
Group:		Development/Languages/Python
%pyrequires_eq	python-devel
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description devel
C header files for numerical modules.

%description devel -l pl.UTF-8
Pliki nagłówkowe języka C modułów numerycznych.

%package numarray
Summary:	Array manipulation and computations for python
Summary(pl.UTF-8):	Operacje i obliczenia na tablicach dla Pythona
Group:		Development/Languages/Python
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description numarray
Numarray provides array manipulation and computational capabilities
similar to those found in IDL, Matlab, or Octave. Using numarray, it
is possible to write many efficient numerical data processing
applications directly in Python without using any C, C++ or Fortran
code (as well as doing such analysis interactively within Python or
PyRAF). For algorithms that are not well suited for efficient
computation using array facilities it is possible to write C functions
(and eventually Fortran) that can read and write numarray arrays that
can be called from Python.

Numarray is a re-implementation of an older Python array module called
Numeric. In general its interface is very similar. It is mostly
backward compatible and will be becoming more so in future releases.

%description numarray -l pl.UTF-8
Numarray zapewnia narzędzia do operacji oraz obliczeń na tablicach
podobne do tych, jakie zapewniają IDL, Matlab czy Octave. Używając
numarray możliwe jest stworzenie bezpośrednio w Pythonie, nie używając
wstawek C, C++ czy fortranowych, wielu wydajnych aplikacji do
przetwarzania danych numerycznych. Dla algorytmów, które nie pracują
wydajnie z tablicami, możliwe jest napisanie funkcji C, które mogą
czytać i zapisywać tablice numarray, i które mogą być wywoływane z
poziomu Pythona.

Numarray jest ponowną implementacją starszego modułu Pythona -
Numeric. Interfejsy tych modułów są do siebie bardzo podobne. Numarray
jest w większości przypadków kompatybilny wstecz, a sytuacja poprawi
się w nowszych wersjach.

%package numarray-devel
Summary:	Header files for python-numarray
Summary(pl.UTF-8):	Pliki nagłówkowe dla python-numarray
Group:		Development/Libraries
Requires:	%{name}-devel = %{epoch}:%{version}-%{release}
Requires:	%{name}-numarray = %{epoch}:%{version}-%{release}

%description numarray-devel
Header files for python-numarray.

%description numarray-devel -l pl.UTF-8
Pliki nagłówkowe dla python-numarray.

%package oldnumeric
Summary:	Old numeric packages
Summary(pl.UTF-8):	Stare pakiety numeric
Group:		Libraries/Python
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description oldnumeric
Old numeric packages.

%description oldnumeric -l pl.UTF-8
Stare pakiety numeric.

%package -n f2py
Summary:	Fortran to Python interface generator
Summary(pl.UTF-8):	Generator interfejsów z Fortranu do Pythona
Group:		Libraries/Python
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description -n f2py
Fortran to Python interface generator.

%description -n f2py -l pl.UTF-8
Generator interfejsów z Fortranu do Pythona.

%prep
%setup -q -n %{module}-%{version}

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
%py_postclean

rm -rf $RPM_BUILD_ROOT%{py_sitedir}/%{module}/{*.txt,COMPATIBILITY,scipy_compatibility,doc}
rm -rf $RPM_BUILD_ROOT%{py_sitedir}/%{module}/*/{tests,docs}
# already in f2py package
rm -rf $RPM_BUILD_ROOT%{py_sitedir}/%{module}/f2py/f2py.1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%dir %{py_sitedir}/%{module}
%{py_sitedir}/%{module}/*.py[co]
%{py_sitedir}/%{module}/tests
%dir %{py_sitedir}/%{module}/core
%{py_sitedir}/%{module}/core/*.py[co]
%attr(755,root,root) %{py_sitedir}/%{module}/core/*.so
%dir %{py_sitedir}/%{module}/distutils
%{py_sitedir}/%{module}/distutils/*.py[co]
#%{py_sitedir}/%{module}/distutils/site.cfg
%dir %{py_sitedir}/%{module}/distutils/command
%{py_sitedir}/%{module}/distutils/command/*.py[co]
%dir %{py_sitedir}/%{module}/distutils/fcompiler
%{py_sitedir}/%{module}/distutils/fcompiler/*.py[co]
%dir %{py_sitedir}/%{module}/fft
%attr(755,root,root) %{py_sitedir}/%{module}/fft/*.so
%{py_sitedir}/%{module}/fft/*.py[co]
%dir %{py_sitedir}/%{module}/lib
%{py_sitedir}/%{module}/lib/*.py[co]
%attr(755,root,root) %{py_sitedir}/%{module}/lib/*.so
%dir %{py_sitedir}/%{module}/linalg
%{py_sitedir}/%{module}/linalg/*.py[co]
%attr(755,root,root) %{py_sitedir}/%{module}/linalg/*.so
%dir %{py_sitedir}/%{module}/random
%{py_sitedir}/%{module}/random/*.py[co]
%attr(755,root,root) %{py_sitedir}/%{module}/random/*.so
%dir %{py_sitedir}/%{module}/testing
%{py_sitedir}/%{module}/testing/*.py[co]
%{py_sitedir}/numpy-*.egg-info

%files devel
%defattr(644,root,root,755)
%{py_sitedir}/%{module}/core/include
%{py_sitedir}/%{module}/random/*.h

%files numarray
%defattr(644,root,root,755)
%dir %{py_sitedir}/%{module}/numarray
%attr(755,root,root) %{py_sitedir}/%{module}/numarray/*.so
%{py_sitedir}/%{module}/numarray/*.py[co]

%files numarray-devel
%defattr(644,root,root,755)
%dir %{py_sitedir}/%{module}/numarray/numpy
%{py_sitedir}/%{module}/numarray/numpy/*

%files oldnumeric
%defattr(644,root,root,755)
%dir %{py_sitedir}/%{module}/oldnumeric
%{py_sitedir}/%{module}/oldnumeric/*

%files -n f2py
%defattr(644,root,root,755)
%attr(744,root,root) %{_bindir}/f2py
%dir %{py_sitedir}/%{module}/f2py
%{py_sitedir}/%{module}/f2py/*.py[co]
%{py_sitedir}/%{module}/f2py/src
%{py_sitedir}/%{module}/f2py/lib
