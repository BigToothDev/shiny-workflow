from shiny import App, render, ui
import pandas as pd
import plotly.graph_objects as go

data_pop_ua_present = pd.read_csv('./app_files/ukr_pop_present.csv', sep=",", decimal=".")
df_present_pop = pd.DataFrame(data_pop_ua_present)
data_pop_ua_resident = pd.read_csv('./app_files/ukr_pop_resident.csv', sep=",", decimal=".")
df_resident_pop = pd.DataFrame(data_pop_ua_resident)

app_ui = ui.page_fluid(
    ui.panel_title("UKRSTAT - Data Visualisation"),
    ui.page_navbar(
        ui.nav_panel("Ukraine population: Present", 
            ui.input_selectize(  
                "selectize",  
                "Select an option below:",  
                {"Urban": "Urban Population", "Rural": "Rural Population", "Total": "Total Population"},  
                selected="Urban"
            ),  
            ui.output_ui("present_pop_plot"),
        ),
        ui.nav_panel("Ukraine population: Resident", 
                     ui.input_selectize(  
                "selectize",  
                "Select an option below:",  
                {"Urban": "Urban Population", "Rural": "Rural Population", "Total": "Total Population"},  
                selected="Urban"
            ),  
            ui.output_ui("present_pop_plot"),
        ),
        id="tab",
    )
)

def server(input, output, session):
    @output
    @render.ui
    def present_pop_plot():
        population_type = input.selectize()
        y = df_present_pop[population_type] * 1000
        x = df_present_pop["Year"]

        fig = go.Figure()

        fig.add_trace(go.Scatter(
            x=x, 
            y=y, 
            mode='lines+markers',
            name=f'{population_type} Population',
            line=dict(color="#008000"),
            marker=dict(color='#008000', size=10),
            hovertemplate="<b>Year:</b> %{x}<br><b>Population:</b> %{y:,.0f}<extra></extra>"
        ))

        fig.update_layout(
            title=f"{population_type} Population Over Time",
            xaxis_title="Year",
            yaxis_title=f"{population_type} Population (in thousands)",
            xaxis=dict(tickmode='linear', dtick=2), 
            hovermode='x unified'
        )
        return ui.HTML(fig.to_html(full_html=False))

    def resident_pop_plot ():

        return
    
app = App(app_ui, server)