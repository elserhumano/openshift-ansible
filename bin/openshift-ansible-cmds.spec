Summary:       OpenShift Operations files for mirror
Name:          openshift-ansible-cmds
Version:       0.0.0
Release:       1%{?dist}
License:       ASL 2.0
URL:           https://github.com/openshift/openshift-ansible
Source0:       %{name}-%{version}.tar.gz
Requires:      python2
BuildRequires: python2-devel
BuildArch:     noarch

%description
Scripts to make it nicer when working with hosts that are defined only by metadata.

%prep
%setup -q

%build

%install
mkdir -p %{buildroot}/usr/bin
mkdir -p %{buildroot}%{python_sitelib}/openshift_ansible
mkdir -p %{buildroot}/etc/bash_completion.d

cp -p ossh oscp opssh %{buildroot}/usr/bin
cp -p awsutil.py %{buildroot}%{python_sitelib}/openshift_ansible
cp -p ossh_bash_completion %{buildroot}/etc/bash_completion.d

%files
/usr/bin/*
%{python_sitelib}/openshift_ansible/*
/etc/bash_completion.d/*

%changelog
