from shiny import App, render, ui
import pandas as pd
import plotly.graph_objects as go

data_pop_ua_present =  {
    "Year": list(range(1990, 2023)),
    "Urban": [34869.2, 35085.2, 35296.9, 35471, 35400.7, 35118.8, 34767.9, 34387.5, 34048.2, 33702.1, 33338.6, 32951.7, 32574.4, 32328.4, 32146.4, 32009.3, 31877.7, 31777.4, 31668.8, 31587.2, 31524.8, 31441.6, 31380.9, 31378.6, 31336.6, 29673.1, 29585, 29482.3, 29371, 29256.7, 29139.3, 28959.6, 28693.7],
    "Rural": [16969.3, 16859.2, 16759.7, 16773.1, 16713.7, 16609.6, 16529.2, 16430.9, 16322.6, 16216, 16091.2, 15971.5, 15882.7, 15675.1, 15476, 15271.5, 15051.8, 14868.6, 14703.9, 14556.5, 14438.1, 14336.9, 14252.7, 14174.4, 14089.6, 13256.2, 13175.5, 13102.2, 13015.4, 12896.5, 12763.1, 12628.8, 12473.6],
    "Total": [51838.5, 51944.4, 52056.6, 52244.1, 52114.4, 51728.4, 51297.1, 50818.4, 50370.8, 49918.1, 49429.8, 48923.2, 48457.1, 48003.5, 47622.4, 47280.8, 46929.5, 46646, 46372.7, 46143.7, 45962.9, 45778.5, 45633.6, 45553, 45426.2, 42929.3, 42760.5, 42584.5, 42386.4, 42153.2, 41902.4, 41588.4, 41167.3]
}
df_present_pop = pd.DataFrame(data_pop_ua_present)

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
    
app = App(app_ui, server)