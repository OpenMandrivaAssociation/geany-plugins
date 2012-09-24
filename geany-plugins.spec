%global geany_plug_docdir %{_defaultdocdir}/%{name}

Name:           geany-plugins
Version:        1.22
Release:        1
Group:          Development/GNOME and GTK+
License:        GPLv2+ and GPLv3+
Summary:        A collection of different plugins for Geany
Url:            http://plugins.geany.org/
Source0:        http://plugins.geany.org/geany-plugins/geany-plugins-%{version}.tar.bz2

BuildRequires:	intltool >= 0.35.0
BuildRequires:  lua-devel enchant-devel gtkspell-devel
BuildRequires:	geany-devel >= %{version}
Requires:       lua

%description

Geany-Plugins is a collection of different plugins for Geany,
a lightweight IDE. It provides a common location for plugin authors
and users with a known infrastructure and support. List of included
plugins:

* addons -- the Addons plugin
* codenav -- the CodeNav plugin
* debugger -- the Debugger plugin
* devhelp -- the devhelp plugin
* geanydoc -- the GeanyDoc plugin
* geanyextrasel -- the GeanyExtraSel plugin
* geanygdb -- the GeanyGDB plugin (disabled by default)
* geanygendoc -- the GeanyGenDoc plugin
* geanyinsertnum -- the GeanyInsertNum plugin
* geanylatex -- the GeanyLaTeX plugin
* geanylipsum -- the GeanyLipsum plugin
* geanylua -- the GeanyLua plugin
* geanyminiscript -- the GeanyMiniScript plugin
* geanypg -- the geanypg plugin
* geanyprj -- the GeanyPrj plugin
* geanysendmail -- the GeanySendmail plugin
* geanyvc -- the GeanyVC plugin
* geniuspaste -- the paste to a pastebin plugin
* gproject -- the GProject plugin
* gtkspell -- GeanyVC's spell-check support
* pretty_printer -- the pretty-printer plugin
* shiftcolumn -- the ShiftColumn plugin
* spellcheck -- the spellcheck plugin
* treebrowser -- the Treebrowser plugin
* tableconvert -- the Tableconvert plugin
* updatechecker -- the Updatechecker plugin
* webhelper -- the WebHelper plugin
* xmlsnippets -- the XMLSnippets plugin
* extra-c-warnings -- extra C Compiler warnings
* cppcheck -- static code analysis using cppcheck


%prep
%setup -q

%build
%configure
%make


%install
%makeinstall_std

# Remove static library *.la files
find %{buildroot} -name '*.la' -exec rm -f '{}' \;

%find_lang %{name}


%files -f %{name}.lang
%defattr(-,root,root)
%doc NEWS README
%{_libdir}/geany-plugins
%{_libdir}/geany/*
%{_datadir}/geany-plugins
%{_iconsdir}/hicolor/*/apps/gproject-*.*
