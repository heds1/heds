## How to capture ggplot messages in a Shiny app
## H Stirrat 20200115

library(ggplot2)
library(shiny)

# define global lists for messages,
# warnings and errors
err_list <- wrn_list <- msg_list <- list() 

# define global counters for messages,
# warnings and errors
err_num <- wrn_num <- msg_num <- 1

insert_na <- function(df) {

        # randomly select row and col indexes
        row_index <- sample(1:dim(df)[1], 1)
        col_index <- sample(1:dim(df)[2], 1)

        # insert NA in selected position
        df[row_index,col_index] <- NA

        # get name of column with NA inserted
        column_with_na <- names(mtcars)[col_index]

        # return list of outputs
        return(
            list(
                df = df,
                row_index = row_index,
                col_index = col_index,
                column_with_na = column_with_na))
}

ui <- {
    fluidPage(

        # limit maximum height of message box
        tags$head(
            tags$style(
                HTML(
                    '
                    #ggplot_messages {
                        max-height: 200px;
                    }
                    '
                ))),
                
        # button row
        fluidRow(
            column(width = 6,
                actionButton(
                    inputId = 'create_warning',
                    label = 'Create a warning')),
            column(width = 6,
                actionButton(
                    inputId = 'create_error',
                    label = 'Create an error!'))),
        # info text row
        fluidRow(
            textOutput('info_text')),
        # plot row
        fluidRow(
            plotOutput('my_plot')),
        # message output row
        fluidRow(
            verbatimTextOutput('ggplot_messages'))
    )
}

server <- function(input, output, session) {

    # instantiate plot_data reactive val
    plot_data <- reactiveValues(text = 'Click on a button to get started.')

    # generate warning upon button click
    observeEvent(input$create_warning, {

        # remove placeholder for app startup
        plot_data$text <- NULL

        # get mtcars with one NA randomly inserted,
        # along with its row and col indices
        new_data <- insert_na(mtcars)

        # populate plot_data reactiveValues
        plot_data$df <- new_data$df
        plot_data$column_with_na = new_data$column_with_na
        plot_data$row = names(mtcars)[new_data$row_index]
        plot_data$col = names(mtcars)[new_data$col_index]
    })

    # generate error upon button click
    observeEvent(input$create_error, {

        # remove placeholder for app startup
        plot_data$text <- NULL

        # make df not a df -- creates error
        plot_data$df <- 5
    })

    # generate information text to accompany plot
    output$info_text <- reactive({

        # do nothing on app start, otherwise, provide information
        if (!is.null(plot_data$text)) {
            paste(plot_data$text)
        } else {
            paste0(
            "Inserted an NA value into the ",
            plot_data$column_with_na,
            " column to generate a ggplot warning. Plotting ",
            plot_data$row,
            " vs ",
            plot_data$col,
            ".")
       }
    })

    # generate reactive ggplot object dependent on plot_data
    plot_object <- reactive({

        # retrieve data to plot from plot_data reactiveVal
        df <- plot_data$df
        x = plot_data$row
        y = plot_data$col

        # plot simple graph
        ggplot(df, aes_string(x = x, y = y)) +
            geom_point()
    })

    my_messages <- reactive({

        # try to print plot_object() -- this generates messages if any are produced
		tryCatch({
			print(plot_object())
			}, message = function(m) {

                # if there are no messages, then return
				if (m$message == "") {
                    return("No messages")

                # otherwise, get the message time, append it to the global
                # msg_list variable, increment the msg_num counter,
                # concatenate all messages into one vector, and return 
                # all messages sorted by most recent. The same process
                # occurs for warnings and errors below.
                } else {
                    msg_time <- paste0(Sys.time())
					msg_list[[msg_time]] <<- paste0("Message ", msg_num, ": ", m$message)
					msg_num <<- msg_num + 1
					all_msgs <- c(msg_list,wrn_list,err_list)
					return(all_msgs[rev(order(as.POSIXct(names(all_msgs))))])
                }

			}, warning = function(w) {
                if (w$message == "") {
                    return("No warnings")
                } else {
                    wrn_time <- paste0(Sys.time())
					wrn_list[[wrn_time]] <<- paste0("Warning ", wrn_num, ": ", w$message)
					wrn_num <<- wrn_num + 1
					all_msgs <- c(msg_list,wrn_list,err_list)
					return(all_msgs[rev(order(as.POSIXct(names(all_msgs))))])
                }

			}, error = function(e) {
				if (e$message == "") {
					return("No errors")
				} else {
                    err_time <- paste0(Sys.time())
					err_list[[err_time]] <<- paste0("Error ", err_num, ": ", e$message)
					err_num <<- err_num + 1
					all_msgs <- c(msg_list,wrn_list,err_list)
					return(all_msgs[rev(order(as.POSIXct(names(all_msgs))))])
			}
		})
	})

    output$my_plot <- renderPlot({
        plot_object()
    })

    output$ggplot_messages <- renderPrint({
        my_messages()
    })

}

shinyApp(ui, server)