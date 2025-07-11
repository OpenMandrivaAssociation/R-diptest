%global packname  diptest
%global rlibdir  %{_libdir}/R/library

Name:             R-%{packname}
Version:          0.75.5
Release:          2
Summary:          Hartigan's dip test statistic for unimodality - corrected code
Group:            Sciences/Mathematics
License:          GPL (>= 2)
URL:              https://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/diptest_0.75-5.tar.gz
BuildRequires:    R-devel Rmath-devel texlive-collection-latex 

%description
Compute Hartigan's dip test statistic for unimodality

%prep
%setup -q -c -n %{packname}

%build

%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%check
%{_bindir}/R CMD check %{packname}

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/html
%doc %{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/extraData
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/libs
