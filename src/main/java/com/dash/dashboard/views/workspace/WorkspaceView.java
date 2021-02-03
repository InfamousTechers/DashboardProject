package com.dash.dashboard.views.workspace;

import com.vaadin.flow.component.button.Button;
import com.vaadin.flow.component.dependency.CssImport;
import com.vaadin.flow.component.notification.Notification;
import com.vaadin.flow.component.orderedlayout.HorizontalLayout;
//import com.vaadin.flow.component.orderedlayout.VerticalLayout;
import com.vaadin.flow.component.textfield.TextField;
import com.vaadin.flow.router.PageTitle;
import com.vaadin.flow.router.Route;
import com.dash.dashboard.views.main.MainView;
import com.vaadin.flow.router.RouteAlias;

@Route(value = "Workspace", layout = MainView.class)
@PageTitle("Workspace")
@CssImport("./styles/views/dashboard/dashboard-view.css")
@RouteAlias(value = "workspace", layout = MainView.class)
public class WorkspaceView extends HorizontalLayout {

    /**
	 *
	 */
	private static final long serialVersionUID = -7468284506066059747L;
	private TextField name;
    private Button sayOle;

    public WorkspaceView() {
        setId("workspace-view");
        name = new TextField("Your name");
        sayOle = new Button("Say Ola");
        add(name, sayOle);
        setVerticalComponentAlignment(Alignment.END, name, sayOle);
        sayOle.addClickListener(e -> {
            Notification.show("Ole " + name.getValue());
        });
    }

}
