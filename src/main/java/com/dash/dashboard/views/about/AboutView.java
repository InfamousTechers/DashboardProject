package com.dash.dashboard.views.about;

import com.vaadin.flow.component.Text;
import com.vaadin.flow.component.html.Div;
import com.vaadin.flow.router.PageTitle;
import com.vaadin.flow.router.Route;
import com.dash.dashboard.views.main.MainView;

@Route(value = "about", layout = MainView.class)
@PageTitle("About")
public class AboutView extends Div {

    /**
	 *
	 */
	private static final long serialVersionUID = 1L;

	public AboutView() {
        setId("about-view");
        add(new Text("Boii this vaadin framework is fire!!!\nLet's make magic!"));
    }

}
