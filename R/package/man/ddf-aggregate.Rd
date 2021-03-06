% Generated by roxygen2: do not edit by hand
% Please edit documentation in R/ddf.R
\docType{methods}
\name{aggregate.formula}
\alias{aggregate,DDF-method}
\alias{aggregate.formula}
\title{Compute Summary Statistics of a Distributed Data Frame's Subsets}
\usage{
aggregate.formula(formula, data, FUN)

\S4method{aggregate}{DDF}(x, agg.cols, by)
}
\arguments{
\item{formula}{in format, \code{y ~ x1 + x2} or \code{cbind(y1,y2) ~ x1 + x2} where \code{x1, x2} are group-by variables and \code{y,y1,y2} are variables to aggregate on.}

\item{data}{a Distributed Data Frame}

\item{FUN}{the aggregate function, currently support mean, median, var, sum.}

\item{x}{a Distributed Data Frame}

\item{agg.cols}{a list of columns to calculate summary statistics}

\item{by}{a list of grouping columns}
}
\value{
a data frame with columns corresponding to the grouping variables in by followed by aggregated columns from data.
}
\description{
Splits a Distributed Data Frame into subsets, computes summary statistics for each, 
and returns the result in a convenient form.
}
\details{
\code{aggregate.formula} is a standard formula interface to \code{daggr}.
}

