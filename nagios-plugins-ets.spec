Name:           nagios-plugins-ets
Version:        1.0
Release:        1%{?dist}
Summary:        test

License:        test
URL:            test
%undefine _disable_source_fetch
#Source0:        https://github.com/liberodark/nrpe-installer/archive/0.8.0-1.tar.gz
Source0:        https://raw.githubusercontent.com/liberodark/nrpe-installer/master/src/check_mem.c
# https://github.com/liberodark/nrpe-installer
#BuildRequires:  
#Requires:       

%description


%prep
env | grep BUILD
env | grep SOURCE

# %%setup -n nrpe-installer-0.8.0-1

%build
#wget https://raw.githubusercontent.com/liberodark/nrpe-installer/master/src/check_mem.c
gcc $RPM_SOURCE_DIR/check_mem.c -o $RPM_BUILD_DIR/check_mem
echo xyz
# %%configure
#make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
install -d -m 0755 $RPM_BUILD_ROOT/usr/lib64/nagios/plugins/
install -m 0755 $RPM_BUILD_DIR/check_mem $RPM_BUILD_ROOT/usr/lib64/nagios/plugins/check_mem
#%make_install


%files
/usr/lib64/nagios/plugins/check_mem

#%doc



%changelog

# %%clean
#rm -rf $RPM_BUILD_ROOT
