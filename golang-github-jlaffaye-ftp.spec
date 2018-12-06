# Run tests in check section
# disabled: it needs a ftp server running for the tests
%bcond_with check

%global goipath         github.com/jlaffaye/ftp
%global commit          2403248fa8cc9f7909862627aa7337f13f8e0bf1

%global common_description %{expand:
A FTP client package for Go.}

%gometa

Name:    %{goname}
Version: 0
Release: 0.5%{?dist}
Summary: A FTP client package for Go
License: ISC
URL:     %{gourl}
Source:  %{gosource}

%if %{with check}
BuildRequires: golang(github.com/stretchr/testify/assert)
%endif

%description
%{common_description}


%package    devel
Summary:    %{summary}
BuildArch:  noarch
 
%description devel
%{common_description}
 
This package contains the source code needed for building packages that import
the %{goipath} Go namespace.


%prep
%gosetup -q


%install
%goinstall


%if %{with check}
%check
%gochecks
%endif


%files devel -f devel.file-list
%license LICENSE
%doc README.md


%changelog
* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.5.git2403248
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.4.20180628git2403248
- Bump to commit 2403248fa8cc9f7909862627aa7337f13f8e0bf1

* Thu Mar 08 2018 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.3.20180314git4274679
- Update with the new Go packaging
- Upstream GIT revision 4274679

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.2.20170927git299b7ff
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Dec 07 2017 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.1.20170927git299b7ff
- Upstream GIT revision 299b7ff

* Mon Jul 24 2017 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.1.20170721git769512c
- First package for Fedora

