#
# Conditional build:
%bcond_without  python2 # CPython 2.x modules
%bcond_without  python3 # CPython 3.x modules

Summary:	Python 2 numerical facilities - deprecated packages
Summary(pl.UTF-8):	Moduły do obliczeń numerycznych dla języka Python 2 - przestarzałe pakiety
Name:		python-numpy-compat
Version:	1.8.2
Release:	3
Epoch:		1
License:	BSD
Group:		Libraries/Python
Source0:	http://downloads.sourceforge.net/numpy/numpy-%{version}.tar.gz
# Source0-md5:	dd8eece8f6fda3a13836de4adbafb0cb
Patch0:		python-numpy-fortran-version.patch
URL:		http://sourceforge.net/projects/numpy/
%if %{with python2}
BuildRequires:	python-devel
%endif
%if %{with python3}
BuildRequires:	python3-devel >= 1:3.3
BuildRequires:	python3-2to3
%endif
BuildRequires:	gcc-fortran
BuildRequires:	lapack-devel >= 3.1.1-2
BuildRequires:	rpm-pythonprov
# -- dropped some time ago
Obsoletes:	python-numpy-Properties
# -- dropped some time ago, should have been released as separate package, but wasn't
Obsoletes:	python-numpy-kinds
# old subpackage, merged into main
Obsoletes:	python-numpy-FFT
# -- dropped during Numeric->numpy transition (ma in main now?)
Obsoletes:	python-numpy-MA
Obsoletes:	python-numpy-RNG
Obsoletes:	python-Numeric
Obsoletes:	python-Numeric-FFT
Obsoletes:	python-Numeric-MA
Obsoletes:	python-Numeric-RNG
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
NumPy is a collection of extension modules to provide high-performance
multidimensional numeric arrays to the Python programming language.

This package contains deprecated modules (numarray and oldnumeric).

%description -l pl.UTF-8
NumPy to zbiór modułów rozszerzeń zapewniających wydajne obliczenia
numeryczne na macierzach wielowymiarowych w języku Python.

Ten pakiet zawiera przestarzałe moduły: numarray i oldnumeric.

%package -n python-numpy-numarray
Summary:	Array manipulation and computations for Python 2
Summary(pl.UTF-8):	Operacje i obliczenia na tablicach dla Pythona 2
Group:		Development/Languages/Python
Requires:	python-numpy >= %{epoch}:%{version}

%description -n python-numpy-numarray
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

This package contains Python 2 module.

%description -n python-numpy-numarray -l pl.UTF-8
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

Ten pakiet zawiera moduł Pythona 2.

%package -n python-numpy-numarray-devel
Summary:	Header files for python-numarray
Summary(pl.UTF-8):	Pliki nagłówkowe dla pakietu python-numarray
Group:		Development/Libraries
Requires:	python-numpy-devel >= %{epoch}:%{version}
Requires:	python-numpy-numarray = %{epoch}:%{version}-%{release}

%description -n python-numpy-numarray-devel
Header files for python-numarray.

%description -n python-numpy-numarray-devel -l pl.UTF-8
Pliki nagłówkowe dla pakietu python-numarray.

%package -n python-numpy-oldnumeric
Summary:	Python 2 modules providing backward compatibility with old Numeric packages
Summary(pl.UTF-8):	Moduły Pythona 2 zapewniające wsteczną kompatybilność ze starymi pakietami Numeric
Group:		Libraries/Python
Requires:	python-numpy >= %{epoch}:%{version}

%description -n python-numpy-oldnumeric
Python 2 modules providing backward compatibility with old Numeric
packages.

%description -n python-numpy-oldnumeric -l pl.UTF-8
Moduły Pythona 2 zapewniające wsteczną kompatybilność ze starymi
pakietami Numeric.

%package -n python3-numpy-numarray
Summary:	Array manipulation and computations for Python 3.x
Summary(pl.UTF-8):	Operacje i obliczenia na tablicach dla Pythona 3.x
Group:		Development/Languages/Python
Requires:	python3-numpy >= %{epoch}:%{version}

%description -n python3-numpy-numarray
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

This package contains Python 3 module.

%description -n python3-numpy-numarray -l pl.UTF-8
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

Ten pakiet zawiera moduł Pythona 3.

%package -n python3-numpy-numarray-devel
Summary:	Header files for python3-numarray
Summary(pl.UTF-8):	Pliki nagłówkowe dla pakietu python3-numarray
Group:		Development/Libraries
Requires:	python3-numpy-devel >= %{epoch}:%{version}
Requires:	python3-numpy-numarray = %{epoch}:%{version}-%{release}

%description -n python3-numpy-numarray-devel
Header files for python3-numarray.

%description -n python3-numpy-numarray-devel -l pl.UTF-8
Pliki nagłówkowe dla pakietu python3-numarray.

%package -n python3-numpy-oldnumeric
Summary:	Python 3 modules providing backward compatibility with old Numeric packages
Summary(pl.UTF-8):	Moduły Pythona 3 zapewniające wsteczną kompatybilność ze starymi pakietami Numeric
Group:		Libraries/Python
Requires:	python3-numpy >= %{epoch}:%{version}

%description -n python3-numpy-oldnumeric
Python 3 modules providing backward compatibility with old Numeric
packages.

%description -n python3-numpy-oldnumeric -l pl.UTF-8
Moduły Pythona 3 zapewniające wsteczną kompatybilność ze starymi
pakietami Numeric.

%prep
%setup -q -n numpy-%{version}
%patch0 -p1

%build
CC="%{__cc}"; export CC
CFLAGS="%{rpmcflags}"; export CFLAGS

%if %{with python2}
%py_build
%endif

%if %{with python3}
%py3_build
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_ocomp $RPM_BUILD_ROOT%{py_sitedir}
%py_comp $RPM_BUILD_ROOT%{py_sitedir}

# leave only numarray and oldnumeric
%{__rm} $RPM_BUILD_ROOT%{_bindir}/f2py
%{__rm} -r $RPM_BUILD_ROOT%{py_sitedir}/numpy/{compat,core,doc,distutils,f2py,fft,lib,linalg,ma,matrixlib,polynomial,random,testing,tests}
%{__rm} $RPM_BUILD_ROOT%{py_sitedir}/numpy/*.py*
%{__rm} $RPM_BUILD_ROOT%{py_sitedir}/numpy-%{version}-py*.egg-info
%{__rm} -r $RPM_BUILD_ROOT%{py_sitedir}/numpy/*/tests
%endif

%if %{with python3}
%py3_install

%py3_ocomp $RPM_BUILD_ROOT%{py3_sitedir}
%py3_comp $RPM_BUILD_ROOT%{py3_sitedir}

# leave only numarray and oldnumeric
%{__rm} $RPM_BUILD_ROOT%{_bindir}/f2py3
%{__rm} -r $RPM_BUILD_ROOT%{py3_sitedir}/numpy/{__pycache__,compat,core,doc,distutils,f2py,fft,lib,linalg,ma,matrixlib,polynomial,random,testing,tests}
%{__rm} $RPM_BUILD_ROOT%{py3_sitedir}/numpy/*.py
%{__rm} $RPM_BUILD_ROOT%{py3_sitedir}/numpy-%{version}-py*.egg-info
%{__rm} -r $RPM_BUILD_ROOT%{py3_sitedir}/numpy/*/tests
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files -n python-numpy-numarray
%defattr(644,root,root,755)
%dir %{py_sitedir}/numpy/numarray
%{py_sitedir}/numpy/numarray/*.py
%{py_sitedir}/numpy/numarray/*.py[co]
%attr(755,root,root) %{py_sitedir}/numpy/numarray/_capi.so

%files -n python-numpy-numarray-devel
%defattr(644,root,root,755)
%{py_sitedir}/numpy/numarray/include

%files -n python-numpy-oldnumeric
%defattr(644,root,root,755)
%dir %{py_sitedir}/numpy/oldnumeric
%{py_sitedir}/numpy/oldnumeric/*.py
%{py_sitedir}/numpy/oldnumeric/*.py[co]
%endif

%if %{with python3}
%files -n python3-numpy-numarray
%defattr(644,root,root,755)
%dir %{py3_sitedir}/numpy/numarray
%{py3_sitedir}/numpy/numarray/*.py
%{py3_sitedir}/numpy/numarray/__pycache__
%attr(755,root,root) %{py3_sitedir}/numpy/numarray/_capi.cpython-3*.so

%files -n python3-numpy-numarray-devel
%defattr(644,root,root,755)
%{py3_sitedir}/numpy/numarray/include

%files -n python3-numpy-oldnumeric
%defattr(644,root,root,755)
%dir %{py3_sitedir}/numpy/oldnumeric
%{py3_sitedir}/numpy/oldnumeric/*.py
%{py3_sitedir}/numpy/oldnumeric/__pycache__
%endif
