from plotnine import ggplot, aes, geom_point
from plotnine.data import diamonds

(
    ggplot(diamonds, aes(x='carat', y='price'))
    + geom_point(alpha=1/20.)
)