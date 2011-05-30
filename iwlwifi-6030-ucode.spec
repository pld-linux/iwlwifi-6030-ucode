Summary:	Microcode image for Intel Centrino Advanced-N 6230, Wireless-N 1030 and Wireless-N 130
Summary(pl.UTF-8):	Obraz mikrokodu dla kart Intel Centrino Advanced-N 6230, Wireless-N 1030 i Wireless-N 130
%define	_fname	6000g2b
%define	_module	6030
Name:		iwlwifi-%{_module}-ucode
Version:	17.168.5.2
Release:	1
License:	distributable
Group:		Base/Kernel
Source0:	http://www.intellinuxwireless.org/iwlwifi/downloads/iwlwifi-6000g2b-ucode-%{version}.tgz
# Source0-md5:	d87411296b4eeda0c91322228e9f8437
URL:		http://www.intellinuxwireless.org/
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The file provided in this package must be present on your system in
order for the Intel Centrino Advanced-N 6230, Wireless-N 1030 and
Wireless-N 130 driver for Linux (iwlwifi-%{_module}) to operate on
your system.

On adapter initialization, and at varying times during the uptime of
the adapter, the microcode is loaded into the RAM on the network
adapter. The microcode provides the low level MAC features including
radio control and high precision timing events (backoff, transmit,
etc.) while also providing varying levels of packet filtering which
can be used to keep the host from having to handle packets that are
not of interest given the current operating mode of the device.

%description -l pl.UTF-8
Plik dostarczany przez ten pakiet jest wymagany w systemie do
działania linuksowego sterownika dla układów bezprzewodowych Intel
Centrino Advanced-N 6230, Wireless-N 1030 i Wireless-N 130
(iwlwifi-%{_module}).

Przy inicjalizacji układu i w różnych chwilach w trakcie jego
działania mikrokod jest wczytywany do pamięci RAM układu. Mikrokod
udostępnia funkcje niskopoziomowe MAC, w tym sterowanie częścią
radiową i zdarzeniami wymagającymi dużej dokładności czasowej
(oczekiwania, transmisja itp.), a także różne poziomy filtrowania
pakietów, zapobiegające docieraniu do komputera pakietów
niepotrzebnych w danym trybie pracy urządzenia.

%prep
%setup -q -n iwlwifi-%{_fname}-ucode-%{version}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/lib/firmware

install iwlwifi-%{_fname}-*.ucode $RPM_BUILD_ROOT/lib/firmware
install LICENSE.* $RPM_BUILD_ROOT/lib/firmware/%{name}-LICENSE

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.*
/lib/firmware/%{name}-LICENSE
/lib/firmware/*.ucode
