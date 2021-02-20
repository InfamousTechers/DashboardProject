package com.dash.dashboard.workspaceClasses;

import com.vaadin.flow.component.icon.VaadinIcon;

public class State {
    VaadinIcon icon;
    String state;

    public State(VaadinIcon icon, String state){
        this.icon = icon;
        this.state = state;
    }

    public String getText(){
        return state;
    }

    public VaadinIcon getIcon(){
        return icon;
    }
}
