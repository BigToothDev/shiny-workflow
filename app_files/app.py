from shiny import App, render, ui, reactive
import pandas as pd
import plotly.graph_objects as go

# data_pop_ua_present = pd.read_csv('./app_files/ukr_pop_present.csv', sep=",", decimal=".")
df_present_pop = pd.DataFrame({
    "Year": list(range(1990, 2023)),
    "Urban": [34869.2, 35085.2, 35296.9, 35471, 35400.7, 35118.8, 34767.9, 34387.5, 34048.2, 33702.1, 33338.6, 32951.7, 32574.4, 32328.4, 32146.4, 32009.3, 31877.7, 31777.4, 31668.8, 31587.2, 31524.8, 31441.6, 31380.9, 31378.6, 31336.6, 29673.1, 29585, 29482.3, 29371, 29256.7, 29139.3, 28959.6, 28693.7],
    "Rural": [16969.3, 16859.2, 16759.7, 16773.1, 16713.7, 16609.6, 16529.2, 16430.9, 16322.6, 16216, 16091.2, 15971.5, 15882.7, 15675.1, 15476, 15271.5, 15051.8, 14868.6, 14703.9, 14556.5, 14438.1, 14336.9, 14252.7, 14174.4, 14089.6, 13256.2, 13175.5, 13102.2, 13015.4, 12896.5, 12763.1, 12628.8, 12473.6],
    "Total": [51838.5, 51944.4, 52056.6, 52244.1, 52114.4, 51728.4, 51297.1, 50818.4, 50370.8, 49918.1, 49429.8, 48923.2, 48457.1, 48003.5, 47622.4, 47280.8, 46929.5, 46646, 46372.7, 46143.7, 45962.9, 45778.5, 45633.6, 45553, 45426.2, 42929.3, 42760.5, 42584.5, 42386.4, 42153.2, 41902.4, 41588.4, 41167.3]
})
# data_pop_ua_resident = pd.read_csv('./app_files/ukr_pop_resident.csv', sep=",", decimal=".")
df_resident_pop = pd.DataFrame({
    "Year": [1990, 1991, 1992, 1993, 1994, 1995, 1996, 1997, 1998, 1999, 2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022],
    "Male": [23826.2, 23886.5, 23949.4, 24046.3, 23981.1, 23792.3, 23591.6, 23366.2, 23163.5, 22963.4, 22754.7, 22530.4, 22316.3, 22112.5, 21926.8, 21754.0, 21574.7, 21434.7, 21297.7, 21185.0, 21107.1, 21032.6, 20976.7, 20962.7, 20918.3, 19787.8, 19717.9, 19644.6, 19558.2, 19455.3, 19343.5, 19195.4, 19007.0],
    "Female": [27730.3, 27737.0, 27758.8, 27824.1, 27734.3, 27508.1, 27282.5, 27033.8, 26810.0, 26581.4, 26360.3, 26133.2, 25924.6, 25710.6, 25515.3, 25346.5, 25174.5, 25031.0, 24894.6, 24778.4, 24675.5, 24565.6, 24476.6, 24410.0, 24327.6, 22971.9, 22873.0, 22770.3, 22658.6, 22528.3, 22389.3, 22223.3, 21990.7],
    "Total": [51556.5, 51623.5, 51708.2, 51870.4, 51715.4, 51300.4, 50874.1, 50400.0, 49973.5, 49544.8, 49115.0, 48663.6, 48240.9, 47823.1, 47442.1, 47100.5, 46749.2, 46465.7, 46192.3, 45963.4, 45782.6, 45598.2, 45453.3, 45372.7, 45245.9, 42759.7, 42590.9, 42414.9, 42216.8, 41983.6, 41732.8, 41418.7, 40997.7]
})
df_by_age_pop = pd.DataFrame({
    "Year": [1990, 1991, 1992, 1993, 1994, 1995, 1996, 1997, 1998, 1999, 2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022],
    "0-14 year": [11084.2, 11029.5, 10951.4, 10915.4, 10767.7, 10528.7, 10246.0, 9952.4, 9624.5, 9206.0, 8781.0, 8373.3, 7949.9, 7569.5, 7246.3, 6989.8, 6764.7, 6606.4, 6501.1, 6476.2, 6483.6, 6496.0, 6531.5, 6620.6, 6710.7, 6449.2, 6494.3, 6535.5, 6530.5, 6481.0, 6386.8, 6279.8, 6119.9],
    "15-64 year": [34297.7, 34264.9, 34248.7, 34264.6, 34084.4, 33810.6, 33569.1, 33394.8, 33322.4, 33437.2, 33515.1, 33446.3, 33312.4, 33060.2, 32826.5, 32603.5, 32417.4, 32256.2, 32184.5, 32169.8, 32130.2, 32137.0, 31993.3, 31846.8, 31606.4, 29634.7, 29327.7, 29011.9, 28719.0, 28468.0, 28199.5, 27927.7, 27646.7],
    "65 years and more": [6174.6, 6329.1, 6508.1, 6690.4, 6863.3, 6961.1, 7059.0, 7052.8, 7026.6, 6901.6, 6818.9, 6844.0, 6978.6, 7193.4, 7369.3, 7507.2, 7567.1, 7603.1, 7506.7, 7317.4, 7168.8, 6965.2, 6928.5, 6905.3, 6928.8, 6675.8, 6768.9, 6867.5, 6967.3, 7034.6, 7146.5, 7211.2, 7231.1],
    "0-15 year": [11814.3, 11762.1, 11690.8, 11625.0, 11489.8, 11248.4, 10988.6, 10673.4, 10366.0, 10012.6, 9571.9, 9144.8, 8743.7, 8315.9, 7966.1, 7664.8, 7408.3, 7218.1, 7071.0, 7005.0, 6982.6, 6975.7, 6993.1, 7047.7, 7120.1, 6816.0, 6856.3, 6887.0, 6895.7, 6862.8, 6786.5, 6678.2, 6550.4],
    "16-59 year": [30291.4, 30230.3, 30314.4, 30523.7, 30646.9, 30595.7, 30424.3, 30166.5, 29793.6, 29500.0, 29353.4, 29259.4, 29154.6, 29314.5, 29514.6, 29656.3, 29812.1, 29799.8, 29738.5, 29586.0, 29328.6, 29090.1, 28842.2, 28622.9, 28372.5, 26613.3, 26317.4, 25982.0, 25641.3, 25293.7, 24968.1, 24618.9, 24294.9],
    "60 years and more": [9450.8, 9631.1, 9703.0, 9721.7, 9578.7, 9456.3, 9461.2, 9560.1, 9813.9, 10032.2, 10189.7, 10259.4, 10342.6, 10192.7, 9961.4, 9779.4, 9528.8, 9447.8, 9382.8, 9372.4, 9471.4, 9532.4, 9618.0, 9702.1, 9753.3, 9330.4, 9417.2, 9545.9, 9679.8, 9827.1, 9978.2, 10121.6, 10152.4],
    "0-17 year": [13305.0, 13225.7, 13148.4, 13101.0, 12937.1, 12668.1, 12416.7, 12124.4, 11823.0, 11469.7, 11116.0, 10740.7, 10307.0, 9878.6, 9503.3, 9129.2, 8802.0, 8536.1, 8325.7, 8186.3, 8081.1, 8003.3, 7971.6, 7990.4, 8009.9, 7614.7, 7614.0, 7615.6, 7609.3, 7579.7, 7533.9, 7459.7, 7348.5],
    "18 years and more": [38251.5, 38397.8, 38559.8, 38769.4, 38778.3, 38632.3, 38457.4, 38275.6, 38150.5, 38075.1, 37999.0, 37922.9, 37933.9, 37944.5, 37938.8, 37971.3, 37947.2, 37929.6, 37866.6, 37777.1, 37701.5, 37594.9, 37481.7, 37382.3, 37236.0, 35145.0, 34976.9, 34799.3, 34607.5, 34403.9, 34198.9, 33959.0, 33649.2],
    "Total": [51556.5, 51623.5, 51708.2, 51870.4, 51715.4, 51300.4, 50874.1, 50400.0, 49973.5, 49544.8, 49115.0, 48663.6, 48240.9, 47823.1, 47442.1, 47100.5, 46749.2, 46465.7, 46192.3, 45963.4, 45782.6, 45598.2, 45453.3, 45372.7, 45245.9, 42759.7, 42590.9, 42414.9, 42216.8, 41983.6, 41732.8, 41418.7, 40997.7]
})

app_ui = ui.page_fluid(
    ui.panel_title("UKRSTAT - Data Visualisation"),
    ui.page_navbar(
        ui.nav_panel("Ukraine population: Present", 
            ui.input_selectize("selectize_present", "Select view:", {
                "Urban": "Urban Population", 
                "Rural": "Rural Population", 
                "Total": "Total Population"
            },  
                selected="Urban"
            ),  
            ui.output_ui("present_pop_plot"),
        ),
        ui.nav_panel("Ukraine population: Resident", 
            ui.input_selectize("selectize_resident", "Select view:", {
                "gender": "Compare by gender",
                "total": "Total Population"
            }, 
                selected="gender"
            ), 
            ui.output_ui("res_pop_plot"),
        ),
        ui.nav_panel("Ukraine population: by Age", 
            ui.input_selectize("selectize_age", "Select view:", {
                "age1g": "0-14 years, 15-64 year, 65+",
                "age2g": "0-15 year, 16-59 year, 60+",
                "age3g": "0-17 year, 18+",
                "total_age": "Total Population"
            }, 
                selected="age1g"
            ), 
            ui.output_ui("age_pop_plot"),
        ),
        id="tab",
    ),
    ui.p("In Accordance: www.ukrstat.gov.ua")
)

def server(input, output, session):
    @reactive.Calc
    def resident_pop_plot():
        if input.selectize_resident() == "gender":
            trace_male = go.Bar(
                x = df_resident_pop ["Year"],
                y = df_resident_pop ["Male"] *1000,
                name = "Male",
                marker_color = "#1fc3aa",
                hovertemplate="<b>Year:</b> %{x}<br><b>Males:</b> %{y:,.0f}<extra></extra>"
            )
            trace_female = go.Bar(
                x = df_resident_pop ["Year"],
                y = df_resident_pop ["Female"] *1000,
                name = "Female",
                marker_color = "#8624f5",
                hovertemplate="<b>Year:</b> %{x}<br><b>Females:</b> %{y:,.0f}<extra></extra>"
            )
            layout = go.Layout(
                title = "Males & Females Population Over Years",
                xaxis = dict(title="Year", tickmode='linear', dtick=2),
                yaxis = dict(title="Population"),
                barmode = "group"
            )
            fig = go.Figure(data=[trace_male, trace_female], layout=layout)
        else:
            trace_total = go.Scatter(
                x = df_resident_pop["Year"],
                y = df_resident_pop["Total"] *1000,
                name = "Total Population",
                mode = "lines+markers",  
                line = dict(color="#7CC674"),
                marker = dict(color="#7CC674", size=10),
                hovertemplate="<b>Year:</b> %{x}<br><b>Total:</b> %{y:,.0f}<extra></extra>"
            )
            layout = go.Layout(
                title = "Total Population Over Years",
                xaxis = dict(title="Year", tickmode='linear', dtick=2),
                yaxis = dict(title="Population"),
                hovermode = 'x unified'
            )
            fig = go.Figure(data=[trace_total], layout=layout)
        return fig
    @reactive.Calc
    def age_pop_plot_calc():
        if input.selectize_age() == "age1g":
            trace_age1g1 = go.Bar(
                x=df_by_age_pop["Year"],
                y=df_by_age_pop["0-14 year"] * 1000,
                name="0-14 year",
                marker_color="#1fc3aa",
                hovertemplate="<b>Year:</b> %{x}<br><b>0-14 year:</b> %{y:,.0f}<extra></extra>"
            )
            trace_age1g2 = go.Bar(
                x=df_by_age_pop["Year"],
                y=df_by_age_pop["15-64 year"] * 1000,
                name="15-64 year",
                marker_color="#8624f5",
                hovertemplate="<b>Year:</b> %{x}<br><b>15-64 year:</b> %{y:,.0f}<extra></extra>"
            )
            trace_age1g3 = go.Bar(
                x=df_by_age_pop["Year"],
                y=df_by_age_pop["65 years and more"] * 1000,
                name="65 years and more",
                marker_color="#f5d024",
                hovertemplate="<b>Year:</b> %{x}<br><b>65 years and more:</b> %{y:,.0f}<extra></extra>"
            )
            layout = go.Layout(
                title="0-14 years, 15-64 year, 65+ Grouped Population Over Years",
                xaxis=dict(title="Year", tickmode='linear', dtick=2),
                yaxis=dict(title="Population"),
                barmode="group"
            )
            fig = go.Figure(data=[trace_age1g1, trace_age1g2, trace_age1g3], layout=layout)
            return fig
        elif input.selectize_age() == "age2g":
            trace_age2g1 = go.Bar(
                x=df_by_age_pop["Year"],
                y=df_by_age_pop["0-15 year"] * 1000,
                name="0-15 year",
                marker_color="#1fc3aa",
                hovertemplate="<b>Year:</b> %{x}<br><b>0-15 year:</b> %{y:,.0f}<extra></extra>"
            )
            trace_age2g2 = go.Bar(
                x=df_by_age_pop["Year"],
                y=df_by_age_pop["16-59 year"] * 1000,
                name="16-59 year",
                marker_color="#8624f5",
                hovertemplate="<b>Year:</b> %{x}<br><b>16-59 year:</b> %{y:,.0f}<extra></extra>"
            )
            trace_age2g3 = go.Bar(
                x=df_by_age_pop["Year"],
                y=df_by_age_pop["60 years and more"] * 1000,
                name="60 years and more",
                marker_color="#f5d024",
                hovertemplate="<b>Year:</b> %{x}<br><b>60 years and more:</b> %{y:,.0f}<extra></extra>"
            )
            layout = go.Layout(
                title="0-15 year, 16-59 year, 60+ Grouped Population Over Years",
                xaxis=dict(title="Year", tickmode='linear', dtick=2),
                yaxis=dict(title="Population"),
                barmode="group"
            )
            fig = go.Figure(data=[trace_age2g1, trace_age2g2, trace_age2g3], layout=layout)
            return fig
        elif input.selectize_age() == "age3g":
            trace_age3g1 = go.Bar(
                x=df_by_age_pop["Year"],
                y=df_by_age_pop["0-17 year"] * 1000,
                name="0-17 year",
                marker_color="#1fc3aa",
                hovertemplate="<b>Year:</b> %{x}<br><b>0-17 year:</b> %{y:,.0f}<extra></extra>"
            )
            trace_age3g2 = go.Bar(
                x=df_by_age_pop["Year"],
                y=df_by_age_pop["18 years and more"] * 1000,
                name="18 years and more",
                marker_color="#8624f5",
                hovertemplate="<b>Year:</b> %{x}<br><b>18 years and more:</b> %{y:,.0f}<extra></extra>"
            )
            layout = go.Layout(
                title="0-17 year, 18+ Grouped Population Over Years",
                xaxis=dict(title="Year", tickmode='linear', dtick=2),
                yaxis=dict(title="Population"),
                barmode="group"
            )
            fig = go.Figure(data=[trace_age3g1, trace_age3g2], layout=layout)
            return fig
        else:
            trace_total = go.Scatter(
                x=df_by_age_pop["Year"],
                y=df_by_age_pop["Total"] * 1000,
                name="Total Population",
                mode="lines+markers",
                line=dict(color="#7CC674"),
                marker=dict(color="#7CC674", size=10),
                hovertemplate="<b>Year:</b> %{x}<br><b>Total:</b> %{y:,.0f}<extra></extra>"
            )
            layout = go.Layout(
                title="Total Population Over Years",
                xaxis=dict(title="Year", tickmode='linear', dtick=2),
                yaxis=dict(title="Population"),
                hovermode='x unified'
            )
            fig = go.Figure(data=[trace_total], layout=layout)
            return fig
    @output
    @render.ui
    def res_pop_plot():
        return resident_pop_plot()
    @output
    @render.ui
    def age_pop_plot():
        return age_pop_plot_calc()
    @output
    @render.ui
    def present_pop_plot():
        population_type = input.selectize_present()
        y = df_present_pop[population_type] * 1000
        x = df_present_pop["Year"]

        fig = go.Figure()

        fig.add_trace(go.Scatter(
            x=x, 
            y=y, 
            mode='lines+markers',
            name=f'{population_type} Population',
            line=dict(color="#7CC674"),
            marker=dict(color='#7CC674', size=10),
            hovertemplate="<b>Year:</b> %{x}<br><b>Population:</b> %{y:,.0f}<extra></extra>"
        ))

        fig.update_layout(
            title=f"{population_type} Population Over Time",
            xaxis_title="Year",
            yaxis_title=f"{population_type} Population",
            xaxis=dict(tickmode='linear', dtick=2), 
            hovermode='x unified'
        )
        return ui.HTML(fig.to_html(full_html=False))
    
app = App(app_ui, server)