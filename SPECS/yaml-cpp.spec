Name:           yaml-cpp
Epoch:          1
Version:        0.6.2
Release:        1%{?dist}
Summary:        A YAML parser and emitter for C++
Group:          Development/Libraries
License:        MIT
URL:            http://code.google.com/p/yaml-cpp/
Source0:        http://yaml-cpp.googlecode.com/files/%{name}-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  boost-devel

%description
yaml-cpp is a YAML parser and emitter in C++ written around the YAML 1.2 spec.


%package        devel
Summary:        Development files for %{name}
Group:          Development/Libraries
License:        MIT
Requires:       %{name}%{?_isa} = %{epoch}:%{version}-%{release}
Requires:       pkgconfig
Requires:       boost-devel

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package        static
Summary:        Static library for %{name}
Group:          Development/Libraries
License:        MIT
Requires:       %{name}-devel%{?_isa} = %{epoch}:%{version}-%{release}

%description    static
The %{name}-static package contains the static library for %{name}.


%prep
%autosetup -p1 -n yaml-cpp-yaml-cpp-%{version}


%build
### Build shared libraries
mkdir build-shared
pushd build-shared
    # ask cmake to not strip binaries
    %cmake -DYAML_CPP_BUILD_TOOLS=0 \
           -DBUILD_SHARED_LIBS=ON \
           ../
    %make_build
popd

### Build static libraries
mkdir build-static
pushd build-static
    # ask cmake to not strip binaries
    %cmake -DYAML_CPP_BUILD_TOOLS=0 \
           -DBUILD_SHARED_LIBS=OFF \
           -DYAML_CPP_BUILD_CONTRIB=OFF \
           ../
    %make_build
popd


%install
pushd build-shared
    %make_install
    rm -rf %{buildroot}/%{_includedir}/gmock/
    rm -rf %{buildroot}/%{_includedir}/gtest/
    rm -rf %{buildroot}/%{_prefix}/lib/libgmock*
    rm -rf %{buildroot}/%{_prefix}/lib/libgtest*
popd

pushd build-static
    %make_install
    rm -rf %{buildroot}/%{_includedir}/gmock/
    rm -rf %{buildroot}/%{_includedir}/gtest/
    rm -rf %{buildroot}/%{_prefix}/lib/libgmock*
    rm -rf %{buildroot}/%{_prefix}/lib/libgtest*
popd


%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig


%files
%doc LICENSE
%{_libdir}/*.so.*

%files devel
%{_includedir}/yaml-cpp/
%{_libdir}/cmake/yaml-cpp/*.cmake
%{_libdir}/*.so
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc

%files static
%license LICENSE
%{_libdir}/*.a


%changelog
* Fri Sep 13 2019 Hiroaki Nakamura <hnakamur@gmail.com> - 1:0.6.2-1
- 0.6.2

* Wed Jul 24 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1:0.5.1-2
- Make yaml-cpp compatible with boost 1.67+

* Sun Jan 28 2018 Richard Shaw <hobbes1069@gmail.com> - 1:0.5.1-1
- Revert epel7 branch back to 0.5.1.
- Add static library package.

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.5.1-7
- Rebuilt for GCC 5 C++11 ABI change

* Thu Feb 26 2015 Guido Grazioli <guido.grazioli@gmail.com> - 0.5.1-6
- Rebuild for gcc switching default to -std=gnu11

* Tue Jan 27 2015 Petr Machata <pmachata@redhat.com> - 0.5.1-5
- Rebuild for boost 1.57.0

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri May 23 2014 Petr Machata <pmachata@redhat.com> - 0.5.1-2
- Rebuild for boost 1.55.0

* Thu Nov 14 2013 Richard Shaw <hobbes1069@gmail.com> - 0.5.1-1
- Update to latest upstream release.

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Feb 10 2012 Richard Shaw <hobbes1069@gmail.com> - 0.3.0-1
- Update to latest release.

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org>
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Sep 30 2011 Guido Grazioli <guido.grazioli@gmail.com> - 0.2.7-1
- Update to 0.2.7
- Remove gcc 4.6 patch fixed upstream

* Mon May 09 2011 Guido Grazioli <guido.grazioli@gmail.com> - 0.2.6-1
- Upstream 0.2.6

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Apr 02 2010 Guido Grazioli <guido.grazioli@gmail.com> - 0.2.5-1
- Upstream 0.2.5

* Fri Jan 15 2010 Guido Grazioli <guido.grazioli@gmail.com> - 0.2.4-1
- Upstream 0.2.4

* Sat Oct 17 2009 Guido Grazioli <guido.grazioli@gmail.com> - 0.2.2-2
- Remove duplicate file

* Wed Oct 14 2009 Guido Grazioli <guido.grazioli@gmail.com> - 0.2.2-1
- Initial packaging 
