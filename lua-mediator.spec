%define debug_package %{nil}

%{!?luaver: %global luaver %(lua -e "print(string.sub(_VERSION, 5))")}
# for arch-independent modules
%global luapkgdir %{_datadir}/lua/%{luaver}

%define vermagic1 1.1.2
%define vermagic2 0

Name:           lua-mediator
Version:        %{vermagic1}_%{vermagic2}
Release:        1%{?dist}
Summary:        A utility class to help you manage events

License:        MIT
URL:            https://github.com/Olivine-Labs/mediator_lua
Source0:        https://github.com/Olivine-Labs/mediator_lua/archive/v%{vermagic1}-%{vermagic2}.tar.gz

BuildArch:      noarch
BuildRequires:  lua-devel >= %{luaver}
%if 0%{?rhel} == 6
Requires:       lua >= %{luaver}
Requires:       lua < 5.2
%else
Requires:       lua(abi) >= %{luaver}
%endif


%description
mediator_lua is a simple class that allows you to listen to events by
subscribing to and sending data to channels. Its purpose is to help you
decouple code where you might otherwise have functions calling functions
calling functions, and instead simply call 'mediator.publish("chat", { message
= "hi" })'.


%prep
%setup -q -n mediator_lua-%{vermagic1}-%{vermagic2}


%build


%install
install -p -m644 -D src/mediator.lua %{buildroot}%{luapkgdir}/mediator.lua


%files
%doc README.md
%{luapkgdir}/mediator.lua


%changelog
* Thu May 19 2016 Jajauma's Packages <jajauma@yandex.ru> - 1.1.2_0-1
- Public release
