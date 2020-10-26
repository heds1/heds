library(shiny)
library(dplyr)
library(ggmap)
library(rvest)
library(tidyr)

# load api key after registering and setting in /etc/R/Renviron.site
register_google(Sys.getenv('GOOGLEMAPS_API_KEY'))

# get table from wikipedia (contains NZ city names)
nz_cities <- read_html('https://en.wikipedia.org/wiki/List_of_cities_in_New_Zealand') %>%
  html_table(fill=TRUE)

# get coordinates
coords <- geocode(nz_cities[[1]]$`Urban area`) %>%
  # add back in names
  mutate(city = nz_cities[[1]]$`Urban area`) %>%
  # join back with rest of table
  left_join(nz_cities[[1]], by = c('city' = 'Urban area')) %>%
  select(-Notes) %>%
  # in case any fail, remove
  drop_na() %>%
  # also remove those with positive lat, e.g.,
  # ones like 'dunedin' that are confused for
  # bigger, northern hemisphere places
  filter(lat < 0) %>%
  # convert pop to numeric
  mutate(Population = as.numeric(gsub(',', '', Population)))

ui <- {
  fluidPage(
    br(),
    fluidRow(
      column(2),
      column(10,
             selectInput('reverse',
                         label = 'South to north',
                         choices = coords %>%
                           arrange(lat) %>%
                           select(city)),
             selectInput('westtoeast',
                         label = 'West to east',
                         choices = coords %>%
                           arrange(lon) %>%
                           select(city)),
             selectInput('tangata',
                         label = 'Population',
                         choices = coords %>%
                           arrange(desc(Population)) %>%
                           select(city)),
             selectInput('third',
                         label = 'Third letter',
                         choices = coords %>%
                           arrange(substr(city, 3,3)) %>%
                           select(city))
      )
    )
  )
}

server <- function(input, output, session) {}

shinyApp(ui, server)