#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cmake
# autospec version: v3
# autospec commit: 750e50d
#
Name     : qt6charts
Version  : 6.6.1
Release  : 7
URL      : https://download.qt.io/official_releases/qt/6.6/6.6.1/submodules/qtcharts-everywhere-src-6.6.1.tar.xz
Source0  : https://download.qt.io/official_releases/qt/6.6/6.6.1/submodules/qtcharts-everywhere-src-6.6.1.tar.xz
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-3-Clause GFDL-1.3 GPL-3.0
Requires: qt6charts-lib = %{version}-%{release}
Requires: qt6charts-license = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : mesa-dev
BuildRequires : qt6base-dev
BuildRequires : qt6declarative-dev
BuildRequires : qt6multimedia-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
---------------
Qt Charts
---------------
Qt Charts module provides a set of easy to use chart components. It uses
the Qt Graphics View Framework, therefore charts can be easily integrated
to modern user interfaces.

%package dev
Summary: dev components for the qt6charts package.
Group: Development
Requires: qt6charts-lib = %{version}-%{release}
Provides: qt6charts-devel = %{version}-%{release}
Requires: qt6charts = %{version}-%{release}

%description dev
dev components for the qt6charts package.


%package lib
Summary: lib components for the qt6charts package.
Group: Libraries
Requires: qt6charts-license = %{version}-%{release}

%description lib
lib components for the qt6charts package.


%package license
Summary: license components for the qt6charts package.
Group: Default

%description license
license components for the qt6charts package.


%prep
%setup -q -n qtcharts-everywhere-src-6.6.1
cd %{_builddir}/qtcharts-everywhere-src-6.6.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1707060237
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
%cmake ..
make  %{?_smp_mflags}
popd
mkdir -p clr-build-avx2
pushd clr-build-avx2
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 "
%cmake ..
make  %{?_smp_mflags}
popd

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1707060237
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/qt6charts
cp %{_builddir}/qtcharts-everywhere-src-%{version}/LICENSES/BSD-3-Clause.txt %{buildroot}/usr/share/package-licenses/qt6charts/b073f11f0c81a95ab5e32aa6b5d23a5955a95274 || :
cp %{_builddir}/qtcharts-everywhere-src-%{version}/LICENSES/GFDL-1.3-no-invariants-only.txt %{buildroot}/usr/share/package-licenses/qt6charts/715f995f11805ee85601834220c43b082f457ea3 || :
cp %{_builddir}/qtcharts-everywhere-src-%{version}/LICENSES/GPL-3.0-only.txt %{buildroot}/usr/share/package-licenses/qt6charts/8624bcdae55baeef00cd11d5dfcfa60f68710a02 || :
pushd clr-build-avx2
%make_install_v3  || :
popd
pushd clr-build
%make_install
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)
/usr/lib64/qt6/metatypes/qt6charts_relwithdebinfo_metatypes.json
/usr/lib64/qt6/metatypes/qt6chartsqml_relwithdebinfo_metatypes.json
/usr/lib64/qt6/mkspecs/modules/qt_lib_charts.pri
/usr/lib64/qt6/mkspecs/modules/qt_lib_charts_private.pri
/usr/lib64/qt6/mkspecs/modules/qt_lib_chartsqml.pri
/usr/lib64/qt6/mkspecs/modules/qt_lib_chartsqml_private.pri
/usr/lib64/qt6/modules/Charts.json
/usr/lib64/qt6/modules/ChartsQml.json
/usr/lib64/qt6/qml/QtCharts/designer/ChartViewSpecifics.qml
/usr/lib64/qt6/qml/QtCharts/designer/default/AreaSeries.qml
/usr/lib64/qt6/qml/QtCharts/designer/default/BarSeries.qml
/usr/lib64/qt6/qml/QtCharts/designer/default/BoxPlotSeries.qml
/usr/lib64/qt6/qml/QtCharts/designer/default/HorizontalBarSeries.qml
/usr/lib64/qt6/qml/QtCharts/designer/default/HorizontalPercentBarSeries.qml
/usr/lib64/qt6/qml/QtCharts/designer/default/HorizontalStackedBarSeries.qml
/usr/lib64/qt6/qml/QtCharts/designer/default/LineSeries.qml
/usr/lib64/qt6/qml/QtCharts/designer/default/PercentBarSeries.qml
/usr/lib64/qt6/qml/QtCharts/designer/default/PieSeries.qml
/usr/lib64/qt6/qml/QtCharts/designer/default/PolarAreaSeries.qml
/usr/lib64/qt6/qml/QtCharts/designer/default/PolarLineSeries.qml
/usr/lib64/qt6/qml/QtCharts/designer/default/PolarScatterSeries.qml
/usr/lib64/qt6/qml/QtCharts/designer/default/PolarSplineSeries.qml
/usr/lib64/qt6/qml/QtCharts/designer/default/ScatterSeries.qml
/usr/lib64/qt6/qml/QtCharts/designer/default/SplineSeries.qml
/usr/lib64/qt6/qml/QtCharts/designer/default/StackedBarSeries.qml
/usr/lib64/qt6/qml/QtCharts/designer/images/areaseries-chart-icon.png
/usr/lib64/qt6/qml/QtCharts/designer/images/areaseries-chart-icon16.png
/usr/lib64/qt6/qml/QtCharts/designer/images/areaseries-polar-icon.png
/usr/lib64/qt6/qml/QtCharts/designer/images/areaseries-polar-icon16.png
/usr/lib64/qt6/qml/QtCharts/designer/images/barseries-icon.png
/usr/lib64/qt6/qml/QtCharts/designer/images/barseries-icon16.png
/usr/lib64/qt6/qml/QtCharts/designer/images/boxplotseries-chart-icon.png
/usr/lib64/qt6/qml/QtCharts/designer/images/boxplotseries-chart-icon16.png
/usr/lib64/qt6/qml/QtCharts/designer/images/horizontalbarseries-icon.png
/usr/lib64/qt6/qml/QtCharts/designer/images/horizontalbarseries-icon16.png
/usr/lib64/qt6/qml/QtCharts/designer/images/horizontalpercentbarseries-icon.png
/usr/lib64/qt6/qml/QtCharts/designer/images/horizontalpercentbarseries-icon16.png
/usr/lib64/qt6/qml/QtCharts/designer/images/horizontalstackedbarseries-icon.png
/usr/lib64/qt6/qml/QtCharts/designer/images/horizontalstackedbarseries-icon16.png
/usr/lib64/qt6/qml/QtCharts/designer/images/lineseries-chart-icon.png
/usr/lib64/qt6/qml/QtCharts/designer/images/lineseries-chart-icon16.png
/usr/lib64/qt6/qml/QtCharts/designer/images/lineseries-polar-icon.png
/usr/lib64/qt6/qml/QtCharts/designer/images/lineseries-polar-icon16.png
/usr/lib64/qt6/qml/QtCharts/designer/images/percentbarseries-icon.png
/usr/lib64/qt6/qml/QtCharts/designer/images/percentbarseries-icon16.png
/usr/lib64/qt6/qml/QtCharts/designer/images/pieseries-chart-icon.png
/usr/lib64/qt6/qml/QtCharts/designer/images/pieseries-chart-icon16.png
/usr/lib64/qt6/qml/QtCharts/designer/images/scatterseries-chart-icon.png
/usr/lib64/qt6/qml/QtCharts/designer/images/scatterseries-chart-icon16.png
/usr/lib64/qt6/qml/QtCharts/designer/images/scatterseries-polar-icon.png
/usr/lib64/qt6/qml/QtCharts/designer/images/scatterseries-polar-icon16.png
/usr/lib64/qt6/qml/QtCharts/designer/images/splineseries-chart-icon.png
/usr/lib64/qt6/qml/QtCharts/designer/images/splineseries-chart-icon16.png
/usr/lib64/qt6/qml/QtCharts/designer/images/splineseries-polar-icon.png
/usr/lib64/qt6/qml/QtCharts/designer/images/splineseries-polar-icon16.png
/usr/lib64/qt6/qml/QtCharts/designer/images/stackedbarseries-icon.png
/usr/lib64/qt6/qml/QtCharts/designer/images/stackedbarseries-icon16.png
/usr/lib64/qt6/qml/QtCharts/designer/qtcharts.metainfo
/usr/lib64/qt6/qml/QtCharts/plugins.qmltypes
/usr/lib64/qt6/qml/QtCharts/qmldir

%files dev
%defattr(-,root,root,-)
/usr/include/QtCharts/6.6.1/QtCharts/private/abstractbarchartitem_p.h
/usr/include/QtCharts/6.6.1/QtCharts/private/abstractchartlayout_p.h
/usr/include/QtCharts/6.6.1/QtCharts/private/abstractdomain_p.h
/usr/include/QtCharts/6.6.1/QtCharts/private/areachartitem_p.h
/usr/include/QtCharts/6.6.1/QtCharts/private/axisanimation_p.h
/usr/include/QtCharts/6.6.1/QtCharts/private/bar_p.h
/usr/include/QtCharts/6.6.1/QtCharts/private/baranimation_p.h
/usr/include/QtCharts/6.6.1/QtCharts/private/barchartitem_p.h
/usr/include/QtCharts/6.6.1/QtCharts/private/boxplotanimation_p.h
/usr/include/QtCharts/6.6.1/QtCharts/private/boxplotchartitem_p.h
/usr/include/QtCharts/6.6.1/QtCharts/private/boxwhiskers_p.h
/usr/include/QtCharts/6.6.1/QtCharts/private/boxwhiskersanimation_p.h
/usr/include/QtCharts/6.6.1/QtCharts/private/boxwhiskersdata_p.h
/usr/include/QtCharts/6.6.1/QtCharts/private/candlestick_p.h
/usr/include/QtCharts/6.6.1/QtCharts/private/candlestickanimation_p.h
/usr/include/QtCharts/6.6.1/QtCharts/private/candlestickbodywicksanimation_p.h
/usr/include/QtCharts/6.6.1/QtCharts/private/candlestickchartitem_p.h
/usr/include/QtCharts/6.6.1/QtCharts/private/candlestickdata_p.h
/usr/include/QtCharts/6.6.1/QtCharts/private/cartesianchartaxis_p.h
/usr/include/QtCharts/6.6.1/QtCharts/private/cartesianchartlayout_p.h
/usr/include/QtCharts/6.6.1/QtCharts/private/chartanimation_p.h
/usr/include/QtCharts/6.6.1/QtCharts/private/chartaxiselement_p.h
/usr/include/QtCharts/6.6.1/QtCharts/private/chartbackground_p.h
/usr/include/QtCharts/6.6.1/QtCharts/private/chartbarcategoryaxisx_p.h
/usr/include/QtCharts/6.6.1/QtCharts/private/chartbarcategoryaxisy_p.h
/usr/include/QtCharts/6.6.1/QtCharts/private/chartcategoryaxisx_p.h
/usr/include/QtCharts/6.6.1/QtCharts/private/chartcategoryaxisy_p.h
/usr/include/QtCharts/6.6.1/QtCharts/private/chartcoloraxisx_p.h
/usr/include/QtCharts/6.6.1/QtCharts/private/chartcoloraxisy_p.h
/usr/include/QtCharts/6.6.1/QtCharts/private/chartconfig_p.h
/usr/include/QtCharts/6.6.1/QtCharts/private/chartdataset_p.h
/usr/include/QtCharts/6.6.1/QtCharts/private/chartdatetimeaxisx_p.h
/usr/include/QtCharts/6.6.1/QtCharts/private/chartdatetimeaxisy_p.h
/usr/include/QtCharts/6.6.1/QtCharts/private/chartelement_p.h
/usr/include/QtCharts/6.6.1/QtCharts/private/charthelpers_p.h
/usr/include/QtCharts/6.6.1/QtCharts/private/chartitem_p.h
/usr/include/QtCharts/6.6.1/QtCharts/private/chartlogvalueaxisx_p.h
/usr/include/QtCharts/6.6.1/QtCharts/private/chartlogvalueaxisy_p.h
/usr/include/QtCharts/6.6.1/QtCharts/private/chartpresenter_p.h
/usr/include/QtCharts/6.6.1/QtCharts/private/charttheme_p.h
/usr/include/QtCharts/6.6.1/QtCharts/private/chartthemebluecerulean_p.h
/usr/include/QtCharts/6.6.1/QtCharts/private/chartthemeblueicy_p.h
/usr/include/QtCharts/6.6.1/QtCharts/private/chartthemebluencs_p.h
/usr/include/QtCharts/6.6.1/QtCharts/private/chartthemebrownsand_p.h
/usr/include/QtCharts/6.6.1/QtCharts/private/chartthemedark_p.h
/usr/include/QtCharts/6.6.1/QtCharts/private/chartthemehighcontrast_p.h
/usr/include/QtCharts/6.6.1/QtCharts/private/chartthemelight_p.h
/usr/include/QtCharts/6.6.1/QtCharts/private/chartthememanager_p.h
/usr/include/QtCharts/6.6.1/QtCharts/private/chartthemeqt_p.h
/usr/include/QtCharts/6.6.1/QtCharts/private/chartthemesystem_p.h
/usr/include/QtCharts/6.6.1/QtCharts/private/charttitle_p.h
/usr/include/QtCharts/6.6.1/QtCharts/private/chartvalueaxisx_p.h
/usr/include/QtCharts/6.6.1/QtCharts/private/chartvalueaxisy_p.h
/usr/include/QtCharts/6.6.1/QtCharts/private/datetimeaxislabel_p.h
/usr/include/QtCharts/6.6.1/QtCharts/private/editableaxislabel_p.h
/usr/include/QtCharts/6.6.1/QtCharts/private/glwidget_p.h
/usr/include/QtCharts/6.6.1/QtCharts/private/glxyseriesdata_p.h
/usr/include/QtCharts/6.6.1/QtCharts/private/horizontalaxis_p.h
/usr/include/QtCharts/6.6.1/QtCharts/private/horizontalbarchartitem_p.h
/usr/include/QtCharts/6.6.1/QtCharts/private/horizontalpercentbarchartitem_p.h
/usr/include/QtCharts/6.6.1/QtCharts/private/horizontalstackedbarchartitem_p.h
/usr/include/QtCharts/6.6.1/QtCharts/private/legendlayout_p.h
/usr/include/QtCharts/6.6.1/QtCharts/private/legendmarkeritem_p.h
/usr/include/QtCharts/6.6.1/QtCharts/private/legendmoveresizehandler_p.h
/usr/include/QtCharts/6.6.1/QtCharts/private/legendscroller_p.h
/usr/include/QtCharts/6.6.1/QtCharts/private/linearrowitem_p.h
/usr/include/QtCharts/6.6.1/QtCharts/private/linechartitem_p.h
/usr/include/QtCharts/6.6.1/QtCharts/private/logxlogydomain_p.h
/usr/include/QtCharts/6.6.1/QtCharts/private/logxlogypolardomain_p.h
/usr/include/QtCharts/6.6.1/QtCharts/private/logxydomain_p.h
/usr/include/QtCharts/6.6.1/QtCharts/private/logxypolardomain_p.h
/usr/include/QtCharts/6.6.1/QtCharts/private/percentbarchartitem_p.h
/usr/include/QtCharts/6.6.1/QtCharts/private/pieanimation_p.h
/usr/include/QtCharts/6.6.1/QtCharts/private/piechartitem_p.h
/usr/include/QtCharts/6.6.1/QtCharts/private/piesliceanimation_p.h
/usr/include/QtCharts/6.6.1/QtCharts/private/pieslicedata_p.h
/usr/include/QtCharts/6.6.1/QtCharts/private/piesliceitem_p.h
/usr/include/QtCharts/6.6.1/QtCharts/private/polarchartaxis_p.h
/usr/include/QtCharts/6.6.1/QtCharts/private/polarchartaxisangular_p.h
/usr/include/QtCharts/6.6.1/QtCharts/private/polarchartaxisradial_p.h
/usr/include/QtCharts/6.6.1/QtCharts/private/polarchartcategoryaxisangular_p.h
/usr/include/QtCharts/6.6.1/QtCharts/private/polarchartcategoryaxisradial_p.h
/usr/include/QtCharts/6.6.1/QtCharts/private/polarchartdatetimeaxisangular_p.h
/usr/include/QtCharts/6.6.1/QtCharts/private/polarchartdatetimeaxisradial_p.h
/usr/include/QtCharts/6.6.1/QtCharts/private/polarchartlayout_p.h
/usr/include/QtCharts/6.6.1/QtCharts/private/polarchartlogvalueaxisangular_p.h
/usr/include/QtCharts/6.6.1/QtCharts/private/polarchartlogvalueaxisradial_p.h
/usr/include/QtCharts/6.6.1/QtCharts/private/polarchartvalueaxisangular_p.h
/usr/include/QtCharts/6.6.1/QtCharts/private/polarchartvalueaxisradial_p.h
/usr/include/QtCharts/6.6.1/QtCharts/private/polardomain_p.h
/usr/include/QtCharts/6.6.1/QtCharts/private/qabstractaxis_p.h
/usr/include/QtCharts/6.6.1/QtCharts/private/qabstractbarseries_p.h
/usr/include/QtCharts/6.6.1/QtCharts/private/qabstractseries_p.h
/usr/include/QtCharts/6.6.1/QtCharts/private/qarealegendmarker_p.h
/usr/include/QtCharts/6.6.1/QtCharts/private/qareaseries_p.h
/usr/include/QtCharts/6.6.1/QtCharts/private/qbarcategoryaxis_p.h
/usr/include/QtCharts/6.6.1/QtCharts/private/qbarlegendmarker_p.h
/usr/include/QtCharts/6.6.1/QtCharts/private/qbarmodelmapper_p.h
/usr/include/QtCharts/6.6.1/QtCharts/private/qbarseries_p.h
/usr/include/QtCharts/6.6.1/QtCharts/private/qbarset_p.h
/usr/include/QtCharts/6.6.1/QtCharts/private/qboxplotlegendmarker_p.h
/usr/include/QtCharts/6.6.1/QtCharts/private/qboxplotmodelmapper_p.h
/usr/include/QtCharts/6.6.1/QtCharts/private/qboxplotseries_p.h
/usr/include/QtCharts/6.6.1/QtCharts/private/qboxset_p.h
/usr/include/QtCharts/6.6.1/QtCharts/private/qcandlesticklegendmarker_p.h
/usr/include/QtCharts/6.6.1/QtCharts/private/qcandlestickmodelmapper_p.h
/usr/include/QtCharts/6.6.1/QtCharts/private/qcandlestickseries_p.h
/usr/include/QtCharts/6.6.1/QtCharts/private/qcandlestickset_p.h
/usr/include/QtCharts/6.6.1/QtCharts/private/qcategoryaxis_p.h
/usr/include/QtCharts/6.6.1/QtCharts/private/qchart_p.h
/usr/include/QtCharts/6.6.1/QtCharts/private/qchartglobal_p.h
/usr/include/QtCharts/6.6.1/QtCharts/private/qchartview_p.h
/usr/include/QtCharts/6.6.1/QtCharts/private/qcoloraxis_p.h
/usr/include/QtCharts/6.6.1/QtCharts/private/qdatetimeaxis_p.h
/usr/include/QtCharts/6.6.1/QtCharts/private/qhorizontalbarseries_p.h
/usr/include/QtCharts/6.6.1/QtCharts/private/qhorizontalpercentbarseries_p.h
/usr/include/QtCharts/6.6.1/QtCharts/private/qhorizontalstackedbarseries_p.h
/usr/include/QtCharts/6.6.1/QtCharts/private/qlegend_p.h
/usr/include/QtCharts/6.6.1/QtCharts/private/qlegendmarker_p.h
/usr/include/QtCharts/6.6.1/QtCharts/private/qlineseries_p.h
/usr/include/QtCharts/6.6.1/QtCharts/private/qlogvalueaxis_p.h
/usr/include/QtCharts/6.6.1/QtCharts/private/qpercentbarseries_p.h
/usr/include/QtCharts/6.6.1/QtCharts/private/qpielegendmarker_p.h
/usr/include/QtCharts/6.6.1/QtCharts/private/qpiemodelmapper_p.h
/usr/include/QtCharts/6.6.1/QtCharts/private/qpieseries_p.h
/usr/include/QtCharts/6.6.1/QtCharts/private/qpieslice_p.h
/usr/include/QtCharts/6.6.1/QtCharts/private/qscatterseries_p.h
/usr/include/QtCharts/6.6.1/QtCharts/private/qsplineseries_p.h
/usr/include/QtCharts/6.6.1/QtCharts/private/qstackedbarseries_p.h
/usr/include/QtCharts/6.6.1/QtCharts/private/qtcharts-config_p.h
/usr/include/QtCharts/6.6.1/QtCharts/private/qtchartsexports_p.h
/usr/include/QtCharts/6.6.1/QtCharts/private/qvalueaxis_p.h
/usr/include/QtCharts/6.6.1/QtCharts/private/qxylegendmarker_p.h
/usr/include/QtCharts/6.6.1/QtCharts/private/qxymodelmapper_p.h
/usr/include/QtCharts/6.6.1/QtCharts/private/qxyseries_p.h
/usr/include/QtCharts/6.6.1/QtCharts/private/scatteranimation_p.h
/usr/include/QtCharts/6.6.1/QtCharts/private/scatterchartitem_p.h
/usr/include/QtCharts/6.6.1/QtCharts/private/scroller_p.h
/usr/include/QtCharts/6.6.1/QtCharts/private/splineanimation_p.h
/usr/include/QtCharts/6.6.1/QtCharts/private/splinechartitem_p.h
/usr/include/QtCharts/6.6.1/QtCharts/private/stackedbarchartitem_p.h
/usr/include/QtCharts/6.6.1/QtCharts/private/valueaxislabel_p.h
/usr/include/QtCharts/6.6.1/QtCharts/private/verticalaxis_p.h
/usr/include/QtCharts/6.6.1/QtCharts/private/xlogydomain_p.h
/usr/include/QtCharts/6.6.1/QtCharts/private/xlogypolardomain_p.h
/usr/include/QtCharts/6.6.1/QtCharts/private/xyanimation_p.h
/usr/include/QtCharts/6.6.1/QtCharts/private/xychart_p.h
/usr/include/QtCharts/6.6.1/QtCharts/private/xydomain_p.h
/usr/include/QtCharts/6.6.1/QtCharts/private/xypolardomain_p.h
/usr/include/QtCharts/QAbstractAxis
/usr/include/QtCharts/QAbstractBarSeries
/usr/include/QtCharts/QAbstractSeries
/usr/include/QtCharts/QAreaLegendMarker
/usr/include/QtCharts/QAreaSeries
/usr/include/QtCharts/QBarCategoryAxis
/usr/include/QtCharts/QBarLegendMarker
/usr/include/QtCharts/QBarModelMapper
/usr/include/QtCharts/QBarSeries
/usr/include/QtCharts/QBarSet
/usr/include/QtCharts/QBoxPlotLegendMarker
/usr/include/QtCharts/QBoxPlotModelMapper
/usr/include/QtCharts/QBoxPlotSeries
/usr/include/QtCharts/QBoxSet
/usr/include/QtCharts/QCandlestickLegendMarker
/usr/include/QtCharts/QCandlestickModelMapper
/usr/include/QtCharts/QCandlestickSeries
/usr/include/QtCharts/QCandlestickSet
/usr/include/QtCharts/QCategoryAxis
/usr/include/QtCharts/QChart
/usr/include/QtCharts/QChartGlobal
/usr/include/QtCharts/QChartView
/usr/include/QtCharts/QColorAxis
/usr/include/QtCharts/QDateTimeAxis
/usr/include/QtCharts/QHBarModelMapper
/usr/include/QtCharts/QHBoxPlotModelMapper
/usr/include/QtCharts/QHCandlestickModelMapper
/usr/include/QtCharts/QHPieModelMapper
/usr/include/QtCharts/QHXYModelMapper
/usr/include/QtCharts/QHorizontalBarSeries
/usr/include/QtCharts/QHorizontalPercentBarSeries
/usr/include/QtCharts/QHorizontalStackedBarSeries
/usr/include/QtCharts/QLegend
/usr/include/QtCharts/QLegendMarker
/usr/include/QtCharts/QLineSeries
/usr/include/QtCharts/QLogValueAxis
/usr/include/QtCharts/QPercentBarSeries
/usr/include/QtCharts/QPieLegendMarker
/usr/include/QtCharts/QPieModelMapper
/usr/include/QtCharts/QPieSeries
/usr/include/QtCharts/QPieSlice
/usr/include/QtCharts/QPolarChart
/usr/include/QtCharts/QScatterSeries
/usr/include/QtCharts/QSplineSeries
/usr/include/QtCharts/QStackedBarSeries
/usr/include/QtCharts/QVBarModelMapper
/usr/include/QtCharts/QVBoxPlotModelMapper
/usr/include/QtCharts/QVCandlestickModelMapper
/usr/include/QtCharts/QVPieModelMapper
/usr/include/QtCharts/QVXYModelMapper
/usr/include/QtCharts/QValueAxis
/usr/include/QtCharts/QXYLegendMarker
/usr/include/QtCharts/QXYModelMapper
/usr/include/QtCharts/QXYSeries
/usr/include/QtCharts/QtCharts
/usr/include/QtCharts/QtChartsDepends
/usr/include/QtCharts/QtChartsVersion
/usr/include/QtCharts/qabstractaxis.h
/usr/include/QtCharts/qabstractbarseries.h
/usr/include/QtCharts/qabstractseries.h
/usr/include/QtCharts/qarealegendmarker.h
/usr/include/QtCharts/qareaseries.h
/usr/include/QtCharts/qbarcategoryaxis.h
/usr/include/QtCharts/qbarlegendmarker.h
/usr/include/QtCharts/qbarmodelmapper.h
/usr/include/QtCharts/qbarseries.h
/usr/include/QtCharts/qbarset.h
/usr/include/QtCharts/qboxplotlegendmarker.h
/usr/include/QtCharts/qboxplotmodelmapper.h
/usr/include/QtCharts/qboxplotseries.h
/usr/include/QtCharts/qboxset.h
/usr/include/QtCharts/qcandlesticklegendmarker.h
/usr/include/QtCharts/qcandlestickmodelmapper.h
/usr/include/QtCharts/qcandlestickseries.h
/usr/include/QtCharts/qcandlestickset.h
/usr/include/QtCharts/qcategoryaxis.h
/usr/include/QtCharts/qchart.h
/usr/include/QtCharts/qchartglobal.h
/usr/include/QtCharts/qchartview.h
/usr/include/QtCharts/qcoloraxis.h
/usr/include/QtCharts/qdatetimeaxis.h
/usr/include/QtCharts/qhbarmodelmapper.h
/usr/include/QtCharts/qhboxplotmodelmapper.h
/usr/include/QtCharts/qhcandlestickmodelmapper.h
/usr/include/QtCharts/qhorizontalbarseries.h
/usr/include/QtCharts/qhorizontalpercentbarseries.h
/usr/include/QtCharts/qhorizontalstackedbarseries.h
/usr/include/QtCharts/qhpiemodelmapper.h
/usr/include/QtCharts/qhxymodelmapper.h
/usr/include/QtCharts/qlegend.h
/usr/include/QtCharts/qlegendmarker.h
/usr/include/QtCharts/qlineseries.h
/usr/include/QtCharts/qlogvalueaxis.h
/usr/include/QtCharts/qpercentbarseries.h
/usr/include/QtCharts/qpielegendmarker.h
/usr/include/QtCharts/qpiemodelmapper.h
/usr/include/QtCharts/qpieseries.h
/usr/include/QtCharts/qpieslice.h
/usr/include/QtCharts/qpolarchart.h
/usr/include/QtCharts/qscatterseries.h
/usr/include/QtCharts/qsplineseries.h
/usr/include/QtCharts/qstackedbarseries.h
/usr/include/QtCharts/qtcharts-config.h
/usr/include/QtCharts/qtchartsexports.h
/usr/include/QtCharts/qtchartsversion.h
/usr/include/QtCharts/qvalueaxis.h
/usr/include/QtCharts/qvbarmodelmapper.h
/usr/include/QtCharts/qvboxplotmodelmapper.h
/usr/include/QtCharts/qvcandlestickmodelmapper.h
/usr/include/QtCharts/qvpiemodelmapper.h
/usr/include/QtCharts/qvxymodelmapper.h
/usr/include/QtCharts/qxylegendmarker.h
/usr/include/QtCharts/qxymodelmapper.h
/usr/include/QtCharts/qxyseries.h
/usr/include/QtChartsQml/6.6.1/QtChartsQml/private/declarativeabstractrendernode_p.h
/usr/include/QtChartsQml/6.6.1/QtChartsQml/private/declarativeareaseries_p.h
/usr/include/QtChartsQml/6.6.1/QtChartsQml/private/declarativeaxes_p.h
/usr/include/QtChartsQml/6.6.1/QtChartsQml/private/declarativebarseries_p.h
/usr/include/QtChartsQml/6.6.1/QtChartsQml/private/declarativeboxplotseries_p.h
/usr/include/QtChartsQml/6.6.1/QtChartsQml/private/declarativecandlestickseries_p.h
/usr/include/QtChartsQml/6.6.1/QtChartsQml/private/declarativecategoryaxis_p.h
/usr/include/QtChartsQml/6.6.1/QtChartsQml/private/declarativechart_p.h
/usr/include/QtChartsQml/6.6.1/QtChartsQml/private/declarativechartglobal_p.h
/usr/include/QtChartsQml/6.6.1/QtChartsQml/private/declarativechartnode_p.h
/usr/include/QtChartsQml/6.6.1/QtChartsQml/private/declarativeforeigntypes_p.h
/usr/include/QtChartsQml/6.6.1/QtChartsQml/private/declarativelineseries_p.h
/usr/include/QtChartsQml/6.6.1/QtChartsQml/private/declarativemargins_p.h
/usr/include/QtChartsQml/6.6.1/QtChartsQml/private/declarativeopenglrendernode_p.h
/usr/include/QtChartsQml/6.6.1/QtChartsQml/private/declarativepieseries_p.h
/usr/include/QtChartsQml/6.6.1/QtChartsQml/private/declarativepolarchart_p.h
/usr/include/QtChartsQml/6.6.1/QtChartsQml/private/declarativescatterseries_p.h
/usr/include/QtChartsQml/6.6.1/QtChartsQml/private/declarativesplineseries_p.h
/usr/include/QtChartsQml/6.6.1/QtChartsQml/private/declarativexypoint_p.h
/usr/include/QtChartsQml/6.6.1/QtChartsQml/private/declarativexyseries_p.h
/usr/include/QtChartsQml/6.6.1/QtChartsQml/private/qtchartsqmlexports_p.h
/usr/include/QtChartsQml/QtChartsQml
/usr/include/QtChartsQml/QtChartsQmlDepends
/usr/include/QtChartsQml/QtChartsQmlVersion
/usr/include/QtChartsQml/qtchartsqmlexports.h
/usr/include/QtChartsQml/qtchartsqmlversion.h
/usr/lib64/cmake/Qt6BuildInternals/StandaloneTests/QtChartsTestsConfig.cmake
/usr/lib64/cmake/Qt6Charts/Qt6ChartsAdditionalTargetInfo.cmake
/usr/lib64/cmake/Qt6Charts/Qt6ChartsConfig.cmake
/usr/lib64/cmake/Qt6Charts/Qt6ChartsConfigVersion.cmake
/usr/lib64/cmake/Qt6Charts/Qt6ChartsConfigVersionImpl.cmake
/usr/lib64/cmake/Qt6Charts/Qt6ChartsDependencies.cmake
/usr/lib64/cmake/Qt6Charts/Qt6ChartsTargets-relwithdebinfo.cmake
/usr/lib64/cmake/Qt6Charts/Qt6ChartsTargets.cmake
/usr/lib64/cmake/Qt6Charts/Qt6ChartsVersionlessTargets.cmake
/usr/lib64/cmake/Qt6ChartsQml/Qt6ChartsQmlAdditionalTargetInfo.cmake
/usr/lib64/cmake/Qt6ChartsQml/Qt6ChartsQmlConfig.cmake
/usr/lib64/cmake/Qt6ChartsQml/Qt6ChartsQmlConfigVersion.cmake
/usr/lib64/cmake/Qt6ChartsQml/Qt6ChartsQmlConfigVersionImpl.cmake
/usr/lib64/cmake/Qt6ChartsQml/Qt6ChartsQmlDependencies.cmake
/usr/lib64/cmake/Qt6ChartsQml/Qt6ChartsQmlTargets-relwithdebinfo.cmake
/usr/lib64/cmake/Qt6ChartsQml/Qt6ChartsQmlTargets.cmake
/usr/lib64/cmake/Qt6ChartsQml/Qt6ChartsQmlVersionlessTargets.cmake
/usr/lib64/cmake/Qt6Qml/QmlPlugins/Qt6qtchartsqml2AdditionalTargetInfo.cmake
/usr/lib64/cmake/Qt6Qml/QmlPlugins/Qt6qtchartsqml2Config.cmake
/usr/lib64/cmake/Qt6Qml/QmlPlugins/Qt6qtchartsqml2ConfigVersion.cmake
/usr/lib64/cmake/Qt6Qml/QmlPlugins/Qt6qtchartsqml2ConfigVersionImpl.cmake
/usr/lib64/cmake/Qt6Qml/QmlPlugins/Qt6qtchartsqml2Targets-relwithdebinfo.cmake
/usr/lib64/cmake/Qt6Qml/QmlPlugins/Qt6qtchartsqml2Targets.cmake
/usr/lib64/libQt6Charts.prl
/usr/lib64/libQt6Charts.so
/usr/lib64/libQt6ChartsQml.prl
/usr/lib64/libQt6ChartsQml.so
/usr/lib64/pkgconfig/Qt6Charts.pc
/usr/lib64/pkgconfig/Qt6ChartsQml.pc

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/libQt6Charts.so.6.6.1
/V3/usr/lib64/libQt6ChartsQml.so.6.6.1
/V3/usr/lib64/qt6/qml/QtCharts/libqtchartsqml2plugin.so
/usr/lib64/libQt6Charts.so.6
/usr/lib64/libQt6Charts.so.6.6.1
/usr/lib64/libQt6ChartsQml.so.6
/usr/lib64/libQt6ChartsQml.so.6.6.1
/usr/lib64/qt6/qml/QtCharts/libqtchartsqml2plugin.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/qt6charts/715f995f11805ee85601834220c43b082f457ea3
/usr/share/package-licenses/qt6charts/8624bcdae55baeef00cd11d5dfcfa60f68710a02
/usr/share/package-licenses/qt6charts/b073f11f0c81a95ab5e32aa6b5d23a5955a95274
