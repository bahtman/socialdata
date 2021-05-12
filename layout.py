####################################################################################################
# Import dash core components (dcc), html and bootstrap components
####################################################################################################

import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import plotly.express as px


from app import app
from filtering import *

####################################################################################################
# FORMATTING INFO
####################################################################################################


####################### CSS formatting #############################################################
dashboard_colors = {
    "superdark-blue": "rgb(31,38,42)",
    "acid-pink": "rgb(213, 3, 160)",
    "black": "rgb(0, 0, 0)",
    "dark-blue-grey": "rgb(103, 117, 126)",
    "medium-blue-grey": "rgb(59,139,235)",
    "dark-blue": "rgb(0,0,0)",
    "superdark-blue": "rgb(31,38,42)",
    "medium-green": "rgb(2,119,189)",
    "light-green": "rgb(245,252,255)",  # This is filter background
    "pink-red": "rgb(178,56,80)",
    "dark-pink-red": "rgb(255, 10, 255)",
    "white": "rgb(251, 251, 252)",
    "light-grey": "rgb(208, 206, 206)",
    "superlight-blue": "rgb(242,242,242)",
    "crimson": "rgb(171, 39, 79)",
    "orange": "rgb(255, 126, 0)",
    "acid-green": "rgb(57, 255, 20)",
}


externalgraph_rowstyling = {"margin-left": "15px", "margin-right": "15px"}

externalgraph_colstyling = {
    "border-radius": "10px",
    "border-style": "solid",
    "border-width": "1px",
    "border-color": dashboard_colors["superlight-blue"],
    "background-color": dashboard_colors["superlight-blue"],
    "box-shadow": "0px 0px 17px 0px rgba(186, 218, 212, .5)",
    "padding-top": "10px",
}

filterdiv_borderstyling = {
    "border-radius": "0px 0px 10px 10px",
    "border-style": "solid",
    "border-width": "1px",
    "border-color": dashboard_colors["light-green"],
    "background-color": dashboard_colors["light-green"],
    "box-shadow": "2px 5px 5px 1px rgba(255, 101, 131, .5)",
}

navbarcurrentpage = {
    "text-decoration": "underline",
    "text-decoration-color": dashboard_colors["white"],
    "text-shadow": "0px 0px 1px rgb(251, 251, 252)",
}

chartdiv = {
    "border-radius": "10px",
    "border-style": "solid",
    "border-width": "1px",
    "border-color": "rgb(251, 251, 252, 0.1)",
    "margin-left": "15px",
    "margin-right": "15px",
    "background-color": dashboard_colors["superdark-blue"],
    "display": "flex",
    "align-items": "center",
    "justify-content": "center",
}

chartdiv_text = {
    "text-align": "left",
    "font-weight": "350",
    "color": dashboard_colors["superdark-blue"],
    "font-size": "1.5rem",
    "letter-spacing": "0.04em",
}

####################### Uniform graphing elements

dashboard_title = {"font": {"size": 16, "color": dashboard_colors["white"]}}

dashboard_xaxis = {
    "showgrid": False,
    "linecolor": dashboard_colors["superdark-blue"],
    "color": dashboard_colors["superdark-blue"],
    "tickangle": 315,
    "titlefont": {"size": 12, "color": dashboard_colors["black"]},
    "tickfont": {"size": 11, "color": dashboard_colors["black"]},
    "zeroline": False,
}

dashboard_yaxis = {
    "showgrid": True,
    "color": dashboard_colors["superdark-blue"],
    "gridwidth": 0.5,
    "gridcolor": dashboard_colors["superdark-blue"],
    "linecolor": dashboard_colors["superdark-blue"],
    "titlefont": {"size": 12, "color": dashboard_colors["superdark-blue"]},
    "tickfont": {"size": 11, "color": dashboard_colors["superdark-blue"]},
    "zeroline": False,
}

dashboard_font_family = "Dosis"

dashboard_legend = {
    "orientation": "h",
    "yanchor": "bottom",
    "y": 1.01,
    "xanchor": "right",
    "x": 1.05,
    "font": {"size": 9, "color": dashboard_colors["superdark-blue"]},
}  # Legend will be on the top right, above the graph, horizontally

dashboard_margins = {
    "l": 5,
    "r": 5,
    "t": 45,
    "b": 15,
}  # Set top margin to in case there is a legend

dashboard_layout = go.Layout(
    font={"family": dashboard_font_family},
    title=dashboard_title,
    title_x=0.5,  # Align chart title to center
    paper_bgcolor="rgba(0,0,0,0)",
    plot_bgcolor="rgba(0,0,0,0)",
    xaxis=dashboard_xaxis,
    yaxis=dashboard_yaxis,
    height=270,
    legend=dashboard_legend,
    margin=dashboard_margins,
)

####################################################################################################
# 000 - DATA MAPPING TBD
####################################################################################################


weekmonth_dict = {"daily": "Daily", "week": "Weekly", "month": "Monthly"}
nbd_groups = get_nbdgroups()

################################################################################################################################################## SET UP END

################################################################################################################################################## SET UP END
# Setup dataframes TBD
################################################################################################################################################## SET UP END


################################################################################################################################################## SET UP END
# Filter  data TBD
################################################################################################################################################## SET UP END


####################################################################################################
# DEFINE REUSABLE COMPONENTS AS FUNCTIONS
####################################################################################################

#####################
# Header with logo
def get_header():

    header = html.Div(
        [
            html.Div(
                [
                    html.Img(
                        src=app.get_asset_url("LogoForDashboard.png"),
                        height="100%",
                        width="auto",
                    )
                ],
                className="col-1",
                style={"vertical-align": "middle"},
            ),  # Same as img width, allowing to have the title centrally aligned
            html.Div(
                [
                    html.H2(
                        children="Seattle Rental Analysis",
                        style={
                            "textAlign": "left",
                            "font-family": "Luminari",
                            "font-weight": "bold",
                            "color": dashboard_colors["acid-pink"],
                        },
                    )
                ],
                className="col-4",
                style={"padding-top": "1%"},
            ),
            html.Div(
                [],
                className="col-7",
                style={"align-items": "center", "padding-top": "1%", "height": "auto"},
            ),
        ],
        className="row",
        style={"height": "2%", "background-color": dashboard_colors["superdark-blue"]},
    )

    return header




def get_emptyrow(h="45px"):
    """This returns an empty row of a defined height"""

    emptyrow = html.Div(
        [html.Div([html.Br()], className="col-12")],
        className="row",
        style={"height": h},
    )
    return emptyrow


#####################
# Common Filter Navbar
def get_filterbar():
    filterNavbar = html.Div(
        [  # This should start an array of  four rows
            # create four rows for each filter and its label.
            html.Div(  # Start First Row
                [
                    html.Div([], className="col-1",),
                    html.Div(
                        [
                            html.H5(
                                children="Pick a Neighborhood:",
                                style={
                                    "text-align": "left",
                                    "color": dashboard_colors["medium-blue-grey"],
                                    "font-weight": "bold",
                                },
                            ),
                        ],
                        className="col-11",
                    ),
                ],
                className="row",
            ),  # End first row
            html.Div(  # Start second filter row
                [
                    html.Div(
                        [
                            html.Div(
                                [
                                    dcc.Dropdown(
                                        id="nbd_dropdown",
                                        options=[
                                            {"label": nbd, "value": nbd,}
                                            for nbd in nbd_groups
                                        ],
                                        value="All",  # Set the default value
                                        multi=False,
                                        style={
                                            "font-size": "13px",
                                            "color": dashboard_colors[
                                                "medium-blue-grey"
                                            ],
                                            "white-space": "nowrap",
                                            "text-overflow": "ellipsis",
                                        },
                                    )
                                ],
                                style={"width": "70%", "margin-top": "5px",},
                            ),
                        ],
                        className="col-12",
                    ),
                ],
                className="row",
            ),  # End second filter row
        ],  # This should end array of filter rows
        className="col-2",
        style=externalgraph_colstyling,
    )  # End of the two column filter div
    return filterNavbar


def get_card(card_id, color):
    return dbc.Card(
        [
            dbc.CardBody(
                [
                    html.P(
                        id=card_id,
                        style={
                            "text-align": "center",
                            "color": color,
                            "font-size": "1rem",
                            "font-weight": "bold",
                            "background-color": dashboard_colors["superdark-blue"],
                            "height": "100%",
                        },
                        className="card-text",
                    )
                ]
            ),
        ],
        style={
            "width": "80%",
            "background-color": dashboard_colors["superdark-blue"],
            "display": "flex",
            "align-items": "center",
            "justify-content": "center",
        },
    )


##########################################
# Row to be filled with KPI elements
def get_KPIrow():
    KPIrow = html.Div(
        [  # Internal row
            html.Div(
                [get_card("total_nbd", dashboard_colors["acid-pink"])],
                className="col-4",
            ),
            html.Div(
                [get_card("avg_price", dashboard_colors["acid-pink"])],
                className="col-4",
            ),
            html.Div(
                [get_card("total_listings", dashboard_colors["acid-pink"])],
                className="col-4",
            ),
        ],
        className="row",
        style=chartdiv,
    )  # Internal row END KPIS row
    return KPIrow


####################################################################
# Returns a div containing a Dash Core Component placement card for a col length = 8
def get_8placementcard():
    placementCard = html.Div(
        [
            dbc.Card(
                [
                    dbc.CardHeader(html.P("Add chart", className="card-title",)),
                    dbc.CardBody(
                        [html.P("    Chart 8-column      ", className="card-text",)]
                    ),
                ],
                style={"width": "30rem"},
            ),  # Card end
        ],
        className="col-8",
        style={
            "width": "100%",
            "display": "flex",
            "align-items": "center",
            "justify-content": "center",
        },
    )
    return placementCard


######################################################################################
# Returns a div containing a Dash Core Component placement card for a col length = 4
def get_4placementcard():
    placementCard = html.Div(
        [
            dbc.Card(
                [
                    dbc.CardHeader(html.P("Add Chart", className="card-title",)),
                    dbc.CardBody(
                        [html.P("     Chart 4-column     ", className="card-text",)]
                    ),
                ],
                style={"width": "30rem"},
            ),  # Card end
        ],
        className="col-4",
        style={
            "width": "100%",
            "display": "flex",
            "align-items": "center",
            "justify-content": "center",
        },
    )
    return placementCard


####################################################################
# Returns a div containing a iFrame holder for a col length = 6
def get_mapcol(map_id, filename="Maps/IndvListingsMap.html"):
    """This file returns a Div element that will contain a iFrame that displays a HTML document

    Args:
        map_id (str) : Id of the map element 
        filename (str, optional): [description]. Defaults to "IndvListingsMap.html".

    Returns:
        [type]: [html div]
    """

    iFrameMap = html.Div(
        [
            html.Iframe(
                id=map_id,
                srcDoc=open(filename, "r").read(),
                width="100%",
                height="500 px",
            ),
        ],
        className="col-6",
        style={
            "width": "100%",
            "height": "100 px",
            "display": "flex",
            "align-items": "center",
            "justify-content": "center",
        },
    )
    return iFrameMap


##########################################
# Row containing two chart columns
def get_twochartrow():
    twoChartRow = html.Div(
        [  # Internal row
            # Chart Column
            get_8placementcard(),
            # Chart Column
            get_4placementcard(),
        ],
        className="row",
        style=chartdiv,
    )
    return twoChartRow


##########################################
# Row containing two map charts columns
def get_mapchartrow(
    firstFile="Maps/IndvListingsMap.html"
):
    twoMapChartRow = html.Div(
        [  # Internal row
            # Chart Column
            get_mapcol("indv_listing_map", firstFile),  # The listing map id
            get_mapcol("nbd_map", secondFile),  # The neighborhood group map id
        ],
        className="row",
        style=externalgraph_rowstyling,
    )
    return twoMapChartRow


##########################################
# Row containing one chart column
def get_lastchartrow():
    lastRow = html.Div(
        [  # Internal row
            html.Div([], className="col-4",),
            html.Div(
                [
                    dbc.Card(
                        [
                            dbc.CardHeader(
                                html.P("Add Chart", className="card-title",)
                            ),
                            dbc.CardBody(
                                [html.P("     A Chart     ", className="card-text",)]
                            ),
                        ],
                        style={"width": "30rem"},
                    ),  # Card end
                ],
                className="col-4",
            ),
            html.Div([], className="col-4",),  # Empty column
        ],
        className="row",
        style=chartdiv,
    )
    return lastRow


##########################################
# Row containing three chart columns
def get_threechartrow():
    threeChartRow = html.Div(
        [  # Internal row This is empty right now
            # Chart Column
            html.Div([], className="col-4",),
            # Chart Column
            html.Div([], className="col-4",),
            # Chart Column
            html.Div([], className="col-4",),
        ],
        className="row",
    )  # Internal row
    return threeChartRow


####################################################################################################
# RENTAL MAIN
####################################################################################################
main = html.Div(
    [
        #####################
        # Row 1 : Header
        get_header(),
        #####################
        # Row 2 :
        html.Div(
            [
                html.Div(  # Start of div with 2-col for filters and 9 col for graphs split
                    [
                        get_filterbar(),
                        html.Div(
                            # This column is to be shared by 4 charts
                            [
                                html.Div(
                                    [
                                        html.Div(
                                            [  # External 10-column
                                                get_KPIrow(),
                                                get_mapchartrow(
                                                    "Maps/IndvListingsMap.html",
                                                    "Maps/NeighborhoodCountMap.html",
                                                ),
                                                # get_lastchartrow(),  # Internal row
                                            ],
                                            className="col-12",
                                            style=externalgraph_colstyling,
                                        ),  # External 10-column
                                        # New div end
                                    ],
                                    className="row",
                                )
                            ],
                            className="col-10",
                            style=externalgraph_colstyling,
                        ),
                    ],  # End of div with 2-col and 10-col split
                    className="row",
                    style=externalgraph_rowstyling,  # External row
                ),  # External row
            ]
        )  # This ends the div after Pagelinks navbar
        #####################
    ]
)