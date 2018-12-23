#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-shinystan
Version  : 2.5.0
Release  : 13
URL      : https://cran.r-project.org/src/contrib/shinystan_2.5.0.tar.gz
Source0  : https://cran.r-project.org/src/contrib/shinystan_2.5.0.tar.gz
Summary  : Interactive Visual and Numerical Diagnostics and Posterior
Group    : Development/Tools
License  : GPL-3.0
Requires: R-DT
Requires: R-colourpicker
Requires: R-dygraphs
Requires: R-gtools
Requires: R-rsconnect
Requires: R-shinyjs
BuildRequires : R-DT
BuildRequires : R-bayesplot
BuildRequires : R-colourpicker
BuildRequires : R-dygraphs
BuildRequires : R-gtools
BuildRequires : R-rsconnect
BuildRequires : R-shiny
BuildRequires : R-shinyjs
BuildRequires : R-shinythemes
BuildRequires : R-threejs
BuildRequires : R-xtable
BuildRequires : R-xts
BuildRequires : clr-R-helpers

%description
Carlo (MCMC) diagnostics and plots and tables helpful for analyzing a
    posterior sample. The interface is powered by the 'Shiny' web
    application framework from 'RStudio' and works with the output of MCMC 
    programs written in any programming language (and has extended 
    functionality for 'Stan' models fit using the 'rstan' and 'rstanarm' 
    packages).

%prep
%setup -q -c -n shinystan

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1525656678

%install
rm -rf %{buildroot}
export SOURCE_DATE_EPOCH=1525656678
export LANG=C
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library shinystan
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library shinystan
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library shinystan
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc -l %{buildroot}/usr/lib64/R/library shinystan|| : 
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/shinystan/DESCRIPTION
/usr/lib64/R/library/shinystan/INDEX
/usr/lib64/R/library/shinystan/Meta/Rd.rds
/usr/lib64/R/library/shinystan/Meta/data.rds
/usr/lib64/R/library/shinystan/Meta/features.rds
/usr/lib64/R/library/shinystan/Meta/hsearch.rds
/usr/lib64/R/library/shinystan/Meta/links.rds
/usr/lib64/R/library/shinystan/Meta/nsInfo.rds
/usr/lib64/R/library/shinystan/Meta/package.rds
/usr/lib64/R/library/shinystan/Meta/vignette.rds
/usr/lib64/R/library/shinystan/NAMESPACE
/usr/lib64/R/library/shinystan/NEWS.md
/usr/lib64/R/library/shinystan/R/shinystan
/usr/lib64/R/library/shinystan/R/shinystan.rdb
/usr/lib64/R/library/shinystan/R/shinystan.rdx
/usr/lib64/R/library/shinystan/ShinyStan/css/ShinyStan.css
/usr/lib64/R/library/shinystan/ShinyStan/css/ShinyStan_datatables.css
/usr/lib64/R/library/shinystan/ShinyStan/css/ShinyStan_dygraphs.css
/usr/lib64/R/library/shinystan/ShinyStan/ggplot_fns.rda
/usr/lib64/R/library/shinystan/ShinyStan/global.R
/usr/lib64/R/library/shinystan/ShinyStan/global_utils.R
/usr/lib64/R/library/shinystan/ShinyStan/helper_functions/gg_theme_elements.R
/usr/lib64/R/library/shinystan/ShinyStan/helper_functions/hmc_diagnostics_helpers.R
/usr/lib64/R/library/shinystan/ShinyStan/helper_functions/shinystan_helpers.R
/usr/lib64/R/library/shinystan/ShinyStan/helper_functions/summary_stats_helpers.R
/usr/lib64/R/library/shinystan/ShinyStan/html/accept_stat.html
/usr/lib64/R/library/shinystan/ShinyStan/html/citation.html
/usr/lib64/R/library/shinystan/ShinyStan/html/contribs.html
/usr/lib64/R/library/shinystan/ShinyStan/html/energy.html
/usr/lib64/R/library/shinystan/ShinyStan/html/home_page_links.html
/usr/lib64/R/library/shinystan/ShinyStan/html/mcse.html
/usr/lib64/R/library/shinystan/ShinyStan/html/ndivergent.html
/usr/lib64/R/library/shinystan/ShinyStan/html/neff.html
/usr/lib64/R/library/shinystan/ShinyStan/html/nleapfrog.html
/usr/lib64/R/library/shinystan/ShinyStan/html/nuts.html
/usr/lib64/R/library/shinystan/ShinyStan/html/rhat.html
/usr/lib64/R/library/shinystan/ShinyStan/html/stepsize.html
/usr/lib64/R/library/shinystan/ShinyStan/html/treedepth.html
/usr/lib64/R/library/shinystan/ShinyStan/markdown/pp_check_tutorial.md
/usr/lib64/R/library/shinystan/ShinyStan/server.R
/usr/lib64/R/library/shinystan/ShinyStan/server_files/debounce.R
/usr/lib64/R/library/shinystan/ShinyStan/server_files/pages/diagnose/ppcheck/ppcheck_helpers.R
/usr/lib64/R/library/shinystan/ShinyStan/server_files/pages/diagnose/ppcheck/server/hists_rep_vs_obs.R
/usr/lib64/R/library/shinystan/ShinyStan/server_files/pages/diagnose/ppcheck/server/hists_resids.R
/usr/lib64/R/library/shinystan/ShinyStan/server_files/pages/diagnose/ppcheck/server/hists_test_statistics.R
/usr/lib64/R/library/shinystan/ShinyStan/server_files/pages/diagnose/ppcheck/server/pp_utils.R
/usr/lib64/R/library/shinystan/ShinyStan/server_files/pages/diagnose/ppcheck/server/rep_vs_resid_rep.R
/usr/lib64/R/library/shinystan/ShinyStan/server_files/pages/diagnose/ppcheck/server/rstanarm.R
/usr/lib64/R/library/shinystan/ShinyStan/server_files/pages/diagnose/ppcheck/server/y_vs_avg_rep.R
/usr/lib64/R/library/shinystan/ShinyStan/server_files/pages/diagnose/ppcheck/ui/pp_get_y_and_yrep.R
/usr/lib64/R/library/shinystan/ShinyStan/server_files/pages/diagnose/server/autocorr.R
/usr/lib64/R/library/shinystan/ShinyStan/server_files/pages/diagnose/server/diagnostics.R
/usr/lib64/R/library/shinystan/ShinyStan/server_files/pages/diagnose/server/multitrace.R
/usr/lib64/R/library/shinystan/ShinyStan/server_files/pages/diagnose/server/rhat_neff_mcse.R
/usr/lib64/R/library/shinystan/ShinyStan/server_files/pages/diagnose/server/summary_stats_sampler.R
/usr/lib64/R/library/shinystan/ShinyStan/server_files/pages/diagnose/ui/multitrace_customize.R
/usr/lib64/R/library/shinystan/ShinyStan/server_files/pages/estimate/server/multiparameter_plot.R
/usr/lib64/R/library/shinystan/ShinyStan/server_files/pages/estimate/server/summary_stats.R
/usr/lib64/R/library/shinystan/ShinyStan/server_files/pages/estimate/server/summary_stats_latex.R
/usr/lib64/R/library/shinystan/ShinyStan/server_files/pages/estimate/ui/multiparam_selectize.R
/usr/lib64/R/library/shinystan/ShinyStan/server_files/pages/explore/server/bivariate.R
/usr/lib64/R/library/shinystan/ShinyStan/server_files/pages/explore/server/density.R
/usr/lib64/R/library/shinystan/ShinyStan/server_files/pages/explore/server/histogram.R
/usr/lib64/R/library/shinystan/ShinyStan/server_files/pages/explore/server/multiview.R
/usr/lib64/R/library/shinystan/ShinyStan/server_files/pages/explore/server/summary_stats_param.R
/usr/lib64/R/library/shinystan/ShinyStan/server_files/pages/explore/server/trivariate.R
/usr/lib64/R/library/shinystan/ShinyStan/server_files/pages/explore/ui/ui_trivariate_select_x.R
/usr/lib64/R/library/shinystan/ShinyStan/server_files/pages/more/notes_and_code.R
/usr/lib64/R/library/shinystan/ShinyStan/server_files/tooltips/tooltips.R
/usr/lib64/R/library/shinystan/ShinyStan/server_files/utilities/extract_sso.R
/usr/lib64/R/library/shinystan/ShinyStan/server_files/utilities/make_param_list_with_groups_sort.R
/usr/lib64/R/library/shinystan/ShinyStan/server_files/utilities/par_samps_reactive.R
/usr/lib64/R/library/shinystan/ShinyStan/server_utils.R
/usr/lib64/R/library/shinystan/ShinyStan/text/quick_mcse.txt
/usr/lib64/R/library/shinystan/ShinyStan/text/quick_neff.txt
/usr/lib64/R/library/shinystan/ShinyStan/text/quick_rhat.txt
/usr/lib64/R/library/shinystan/ShinyStan/ui.R
/usr/lib64/R/library/shinystan/ShinyStan/ui_files/PAGE_diagnose.R
/usr/lib64/R/library/shinystan/ShinyStan/ui_files/PAGE_estimate.R
/usr/lib64/R/library/shinystan/ShinyStan/ui_files/PAGE_explore.R
/usr/lib64/R/library/shinystan/ShinyStan/ui_files/PAGE_home.R
/usr/lib64/R/library/shinystan/ShinyStan/ui_files/PAGE_more_menu.R
/usr/lib64/R/library/shinystan/ShinyStan/ui_files/about.R
/usr/lib64/R/library/shinystan/ShinyStan/ui_files/autocorr_customize.R
/usr/lib64/R/library/shinystan/ShinyStan/ui_files/bivariate_customize.R
/usr/lib64/R/library/shinystan/ShinyStan/ui_files/density_customize.R
/usr/lib64/R/library/shinystan/ShinyStan/ui_files/diagnostics_by_parameter.R
/usr/lib64/R/library/shinystan/ShinyStan/ui_files/diagnostics_customize.R
/usr/lib64/R/library/shinystan/ShinyStan/ui_files/diagnostics_energy.R
/usr/lib64/R/library/shinystan/ShinyStan/ui_files/diagnostics_help.R
/usr/lib64/R/library/shinystan/ShinyStan/ui_files/diagnostics_ndivergent.R
/usr/lib64/R/library/shinystan/ShinyStan/ui_files/diagnostics_sample.R
/usr/lib64/R/library/shinystan/ShinyStan/ui_files/diagnostics_stepsize.R
/usr/lib64/R/library/shinystan/ShinyStan/ui_files/diagnostics_treedepth.R
/usr/lib64/R/library/shinystan/ShinyStan/ui_files/dynamic_trace_helptext.R
/usr/lib64/R/library/shinystan/ShinyStan/ui_files/glossary.R
/usr/lib64/R/library/shinystan/ShinyStan/ui_files/help.R
/usr/lib64/R/library/shinystan/ShinyStan/ui_files/hist_customize.R
/usr/lib64/R/library/shinystan/ShinyStan/ui_files/model_code.R
/usr/lib64/R/library/shinystan/ShinyStan/ui_files/multiparam_customize.R
/usr/lib64/R/library/shinystan/ShinyStan/ui_files/notepad.R
/usr/lib64/R/library/shinystan/ShinyStan/ui_files/pp_about.R
/usr/lib64/R/library/shinystan/ShinyStan/ui_files/pp_navlist.R
/usr/lib64/R/library/shinystan/ShinyStan/ui_files/pp_navlist_rstanarm.R
/usr/lib64/R/library/shinystan/ShinyStan/ui_files/rhat_neff_mcse_layout.R
/usr/lib64/R/library/shinystan/ShinyStan/ui_files/sampler_stats_customize.R
/usr/lib64/R/library/shinystan/ShinyStan/ui_files/table_customize.R
/usr/lib64/R/library/shinystan/ShinyStan/ui_files/table_latex_main.R
/usr/lib64/R/library/shinystan/ShinyStan/ui_files/table_latex_sidebar.R
/usr/lib64/R/library/shinystan/ShinyStan/ui_files/trivariate_customize.R
/usr/lib64/R/library/shinystan/ShinyStan/ui_files/trivariate_select.R
/usr/lib64/R/library/shinystan/ShinyStan/ui_utils.R
/usr/lib64/R/library/shinystan/ShinyStan/www/stan_logo.png
/usr/lib64/R/library/shinystan/ShinyStan/www/wide_ensemble.png
/usr/lib64/R/library/shinystan/ShinyStan/www/wide_funnel.png
/usr/lib64/R/library/shinystan/data/Rdata.rdb
/usr/lib64/R/library/shinystan/data/Rdata.rds
/usr/lib64/R/library/shinystan/data/Rdata.rdx
/usr/lib64/R/library/shinystan/doc/deploy_shinystan.Rmd
/usr/lib64/R/library/shinystan/doc/deploy_shinystan.html
/usr/lib64/R/library/shinystan/doc/index.html
/usr/lib64/R/library/shinystan/doc/shinystan-package.Rmd
/usr/lib64/R/library/shinystan/doc/shinystan-package.html
/usr/lib64/R/library/shinystan/help/AnIndex
/usr/lib64/R/library/shinystan/help/aliases.rds
/usr/lib64/R/library/shinystan/help/figures/stanlogo.png
/usr/lib64/R/library/shinystan/help/paths.rds
/usr/lib64/R/library/shinystan/help/shinystan.rdb
/usr/lib64/R/library/shinystan/help/shinystan.rdx
/usr/lib64/R/library/shinystan/html/00Index.html
/usr/lib64/R/library/shinystan/html/R.css
