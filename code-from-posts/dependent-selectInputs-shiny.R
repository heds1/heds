## How to create dependent, bypassable selectizeInputs in a Shiny app
## H Stirrat 20200204

library(dplyr)
library(shiny)

ui <- {
    fluidPage(
        fluidRow(
            selectizeInput(
                inputId = 'select_cyl',
                label = 'Cyl',
                choices = c('All cylinders', sort(unique(mtcars$cyl))),
                multiple = TRUE,
                selected = 'All cylinders'),
            uiOutput(
                outputId = 'select_carb')
        )
    )
}

server <- function(input, output, session) {
    
    # render the child dropdown menu
    output$select_carb <- renderUI({

        # check whether user wants to filter by cyl;
        # if not, then filter by selection
        if ('All cylinders' %in% input$select_cyl) {
            df <- mtcars
        } else {
            df <- mtcars %>%
                filter(
                    cyl %in% input$select_cyl)
        }

        # get available carb values
        carbs <- sort(unique(df$carb))

        # render selectizeInput
        selectizeInput(
            inputId = 'select_carb',
            label = 'Carb',
            choices = c('All carburetors', carbs),
            multiple = TRUE,
            selected = 'All carburetors')
    })

}

shinyApp(ui, server)