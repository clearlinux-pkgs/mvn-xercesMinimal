#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : mvn-xercesMinimal
Version  : 1.9.6.2
Release  : 3
URL      : https://repo1.maven.org/maven2/nekohtml/xercesMinimal/1.9.6.2/xercesMinimal-1.9.6.2.jar
Source0  : https://repo1.maven.org/maven2/nekohtml/xercesMinimal/1.9.6.2/xercesMinimal-1.9.6.2.jar
Source1  : https://repo1.maven.org/maven2/nekohtml/xercesMinimal/1.9.6.2/xercesMinimal-1.9.6.2.pom
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0
Requires: mvn-xercesMinimal-data = %{version}-%{release}

%description
No detailed description available

%package data
Summary: data components for the mvn-xercesMinimal package.
Group: Data

%description data
data components for the mvn-xercesMinimal package.


%prep

%build

%install
mkdir -p %{buildroot}/usr/share/java/.m2/repository/nekohtml/xercesMinimal/1.9.6.2
cp %{SOURCE0} %{buildroot}/usr/share/java/.m2/repository/nekohtml/xercesMinimal/1.9.6.2

mkdir -p %{buildroot}/usr/share/java/.m2/repository/nekohtml/xercesMinimal/1.9.6.2
cp %{SOURCE1} %{buildroot}/usr/share/java/.m2/repository/nekohtml/xercesMinimal/1.9.6.2


%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/java/.m2/repository/nekohtml/xercesMinimal/1.9.6.2/xercesMinimal-1.9.6.2.jar
/usr/share/java/.m2/repository/nekohtml/xercesMinimal/1.9.6.2/xercesMinimal-1.9.6.2.pom
