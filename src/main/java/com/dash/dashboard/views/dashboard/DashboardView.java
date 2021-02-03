package com.dash.dashboard.views.dashboard;

//import com.vaadin.flow.component.Component;
//import com.vaadin.flow.component.button.Button;
import com.vaadin.flow.component.dependency.CssImport;
//import com.vaadin.flow.component.notification.Notification;
import com.vaadin.flow.component.orderedlayout.HorizontalLayout;
import com.vaadin.flow.component.tabs.Tab;
import com.vaadin.flow.component.tabs.Tabs;
//import com.vaadin.flow.component.orderedlayout.VerticalLayout;
//import com.vaadin.flow.component.textfield.TextField;
import com.vaadin.flow.router.PageTitle;
import com.vaadin.flow.router.Route;
import com.dash.dashboard.views.main.MainView;
import com.vaadin.flow.router.RouteAlias;

@Route(value = "Dashboard", layout = MainView.class)
@PageTitle("Dashboard")
@CssImport("./styles/views/dashboard/dashboard-view.css")
@RouteAlias(value = "", layout = MainView.class)
public class DashboardView extends HorizontalLayout {

    /**
	 *
	 */
	private static final long serialVersionUID = -7468284506066059747L;
    private Tabs tabs;
    
    public DashboardView() {
        setId("dashboard-view");
        add(dashTabs());
    }

    private Tabs dashTabs(){
        Tab emails = new Tab("Announcements");
        Tab assignments = new Tab("Pending Assignments");
        Tab tests = new Tab("Upcoming Tests");
        Tab gradebook = new Tab("Gradebook");
        tabs = new Tabs(emails, assignments, tests, gradebook);
        return tabs;
    }

}
