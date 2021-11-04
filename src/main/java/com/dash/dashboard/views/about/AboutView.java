package com.dash.dashboard.views.about;

import com.vaadin.flow.component.html.Div;
import com.vaadin.flow.component.html.H2;
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
        add(new H2("Basic workspace tools web application created by Comfort Twala and Brandon Pahla with Vaadin Java Framework."));
    }

}
