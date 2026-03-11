install.packages("devtools")
devtools::install_github("mattflor/chorddiag", build_vignettes = TRUE)
hrbrthemes::import_roboto_condensed()

library(tidyverse)
library(viridisLite)
library(viridis)
library(patchwork)
library(hrbrthemes)
library(circlize)
library(chorddiag)

chord_data=data.frame(chordsdata)
chord_data=chord_data[-c(1:4,18:19)]
correlation_mat = cor(chord_data)
df = data.frame(from = rep(rownames(correlation_mat), times = ncol(correlation_mat)),
                to = rep(colnames(correlation_mat), each = nrow(correlation_mat)),
                value = as.vector(correlation_mat),
                stringsAsFactors = FALSE)
df = df[df$value != 1,]
df = unique(t(apply(df, 1, sort)))
rownames(df) = 1:nrow(df)
colnames(df) = c("value","from", "to")
df = df[, c(3,1,2)]
df = df[, c(1,3,2)]
df = data.frame(df[, c(2,1,3)])



# parameters
circos.clear()
circos.par(start.degree = 90, gap.degree = 8, track.margin = c(-0.05, 0.05), points.overflow.warning = FALSE)

par(mar = rep(0, 4))

mycolor = viridis(13, alpha = 1, begin = 0, end = 1, option = "D")
mycolor = mycolor[sample(1:13)]

chordDiagram(
  x = df, 
  grid.col = mycolor,
  transparency = 0.1,
  directional = 1,
  direction.type = c("arrows", "diffHeight"), 
  diffHeight  = -0.04,
  annotationTrack = "grid", 
  #annotationTrackHeight = c(0.05, 0.1),
  preAllocateTracks = list(track.height = 0.065),
  link.arr.type = "big.arrow", 
  link.sort = TRUE,
  link.largest.ontop = TRUE,
  #link.lwd = 1,    # Line width
  #link.lty = 1,    # Line type
  #link.border = 1,
  keep.diagonal=FALSE)

# Add text and axis
circos.trackPlotRegion(
  track.index = 1, 
  bg.border = NA, 
  panel.fun = function(x, y) {
    
    xlim = get.cell.meta.data("xlim")
    sector.index = get.cell.meta.data("sector.index")
    
    # Add names to the sector. 
    circos.text(
      x = mean(xlim), 
      y = 3.2, 
      labels = sector.index, 
      facing = "bending.inside", 
      cex = 0.8
    )
    
    #Add graduation on axis
    circos.axis(
      h = "top", 
      major.at = seq(from = 0, to = xlim[2], by = ifelse(test = xlim[2]>14, yes = 4, no = 4)),
      #major.at = seq(from = 0, to = xlim[2], by = ifelse(test = xlim[2]>10, yes = 2, no = 1)),
      minor.ticks = 4, 
      major.tick.length = 0.5,
      labels.facing = "reverse.clockwise",
      labels.niceFacing = FALSE)
    
  }
)






