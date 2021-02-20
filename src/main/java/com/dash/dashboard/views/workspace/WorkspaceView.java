package com.dash.dashboard.views.workspace;

import com.vaadin.flow.component.button.Button;
import com.vaadin.flow.component.button.ButtonVariant;
import com.vaadin.flow.component.dependency.CssImport;
import com.vaadin.flow.component.details.Details;
import com.vaadin.flow.component.details.DetailsVariant;
import com.vaadin.flow.component.dialog.Dialog;
import com.vaadin.flow.component.grid.Grid;
import com.vaadin.flow.component.grid.GridVariant;
import com.vaadin.flow.component.html.Div;
import com.vaadin.flow.component.html.H3;
import com.vaadin.flow.component.html.Span;
import com.vaadin.flow.component.icon.Icon;
import com.vaadin.flow.component.icon.VaadinIcon;
import com.vaadin.flow.component.notification.Notification;
import com.vaadin.flow.component.orderedlayout.HorizontalLayout;
import com.vaadin.flow.component.tabs.Tab;
import com.vaadin.flow.component.tabs.Tabs;
import com.vaadin.flow.component.orderedlayout.FlexLayout;
import com.vaadin.flow.component.orderedlayout.VerticalLayout;
import com.vaadin.flow.component.select.Select;
import com.vaadin.flow.component.textfield.TextArea;
import com.vaadin.flow.component.textfield.TextField;
import com.vaadin.flow.data.provider.ListDataProvider;
import com.vaadin.flow.data.renderer.ComponentRenderer;
import com.vaadin.flow.router.PageTitle;
import com.vaadin.flow.router.Route;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

import com.dash.dashboard.views.main.MainView;
import com.dash.dashboard.workspaceClasses.State;
import com.dash.dashboard.workspaceClasses.Task;
import com.vaadin.flow.router.RouteAlias;
import com.vaadin.flow.component.Component;
import com.vaadin.flow.component.Text;
//import org.springframework.beans.factory.annotation.Autowired;

@Route(value = "Workspace", layout = MainView.class)
@PageTitle("Workspace")
@CssImport("./styles/views/dashboard/dashboard-view.css")
@RouteAlias(value = "workspace", layout = MainView.class)
public class WorkspaceView extends VerticalLayout {

    private static final long serialVersionUID = -7468284506066059747L;
    private Tabs tabs;

    public WorkspaceView() {
        setId("dashboard-view");
        workspaceTabs();
    }

    private void workspaceTabs() {
        // Creating workspace tabs
        Tab todo = new Tab("To-do List");
        Div todoPage = new Div();
        todoFunc(todoPage);

        Tab note = new Tab("Notes");
        Div notePage = new Div();
        noteFunc(notePage);

        Tab calc = new Tab("Calculator");
        Div calcPage = new Div();
        calcFunc(calcPage);

        Tab timer = new Tab("Pomodoro Timer");
        Div timerPage = new Div();
        timerFunc(timerPage);

        Tab cal = new Tab("Calender");
        Div calPage = new Div();
        calFunc(calPage);

        Map<Tab, Component> tabsToPages = new HashMap<>();
        tabsToPages.put(todo, todoPage);
        tabsToPages.put(note, notePage);
        tabsToPages.put(calc, calcPage);
        tabsToPages.put(timer, timerPage);
        tabsToPages.put(cal, calPage);
        tabs = new Tabs(todo, note, calc, timer, cal);
        tabs.setFlexGrowForEnclosedTabs(1);
        Div pages = new Div(todoPage, notePage, calcPage, timerPage, calPage);

        tabs.addSelectedChangeListener(event -> {
            tabsToPages.values().forEach(page -> page.setVisible(false));
            Component selectedPage = tabsToPages.get(tabs.getSelectedTab());
            selectedPage.setVisible(true);
        });

        tabs.setSelectedTab(cal);
        tabs.setSelectedTab(todo);

        add(tabs, pages);
    }

    /**
     * Functions for the pages
     */

    private void todoFunc(Div Page) {
        Page.add(new H3("To-do List"));

        List<Task> tasks = new ArrayList<>();
        Grid<Task> taskGrid = new Grid<>();

        taskGrid.setItems(tasks);
        taskGrid.addComponentColumn(item -> taskStatus()).setHeader("Status").setWidth("20%");
        taskGrid.addColumn(Task::getTask).setHeader("Task").setWidth("70%");
        taskGrid.addComponentColumn(item -> createRemoveButton(taskGrid, item)).setHeader("").setKey("del").setWidth("10%");
        taskGrid.addThemeVariants(GridVariant.LUMO_WRAP_CELL_CONTENT, GridVariant.LUMO_NO_BORDER, GridVariant.LUMO_NO_ROW_BORDERS, GridVariant.LUMO_ROW_STRIPES);

        Button addTask = new Button("Add Task", new Icon(VaadinIcon.PLUS), event -> {
            Dialog taskDialog = new Dialog();
            TextField task = new TextField();
            task.setLabel("What do you have to do?");
            task.setWidth("400px");
            taskDialog.open();
            Button add = new Button(new Icon(VaadinIcon.PLUS), evt -> {
                tasks.add(new Task(task.getValue()));
                taskGrid.getDataProvider().refreshAll();
                Notification.show("Task Added.");
                taskDialog.close();
            });
            add.addThemeVariants(ButtonVariant.LUMO_ICON);
            taskDialog.add(new H3("Add Task"), task, add);
        });

        Page.add(addTask, taskGrid);
    }

    private void noteFunc(Div Page){
        Page.add(new H3("Notes"));

        Button addNote = new Button("Add Note", new Icon(VaadinIcon.PLUS), event -> {
            VerticalLayout noteLayout = new VerticalLayout();
            Dialog noteDialog = new Dialog();
            TextField noteHeader = new TextField();
            noteHeader.setLabel("Title");
            TextArea note = new TextArea("Body");
            noteDialog.open();
            Button add = new Button(new Icon(VaadinIcon.PLUS), evt -> {
                VerticalLayout addLayout = new VerticalLayout();
                Details noteDetails = new Details();
                noteDetails.setSummaryText(noteHeader.getValue());
                Button del = new Button(new Icon(VaadinIcon.TRASH), e -> {
                    Page.remove(noteDetails);
                });
                del.addThemeVariants(ButtonVariant.LUMO_SMALL, ButtonVariant.LUMO_TERTIARY);
                addLayout.add(new Text(note.getValue()), del);
                noteDetails.addContent(addLayout);
                noteDetails.addThemeVariants(DetailsVariant.FILLED);
                Page.add(noteDetails);
                Notification.show("Note (" + noteHeader.getValue() + ") added.");
                noteDialog.close();
            });
            add.addThemeVariants(ButtonVariant.LUMO_ICON);
            noteDialog.add(noteLayout);
            noteLayout.add(noteHeader, note, add);
        });
        Page.add(addNote);
    }

    private void calcFunc(Div Page){
        Page.add(new H3("Calculator"));
        HorizontalLayout calcDivs = new HorizontalLayout();
        Div calc = new Div();
        calc.setWidth("50%");
        Div calcHistory = new Div();
        Details hisDetails = new Details();
        hisDetails.setSummaryText("History");
        VerticalLayout calcHisLayout = new VerticalLayout();

        // Calculator
        TextField display = new TextField();
        display.setLabel(" ");
        display.setValue("0");
        display.setWidth("70%");


        HorizontalLayout row1 = new HorizontalLayout();
        Button lBrac = new Button("(", click -> {
            updateCalc(display, "(");
        });
        Button clearEntered = new Button("CE", click -> {
            display.setValue("0");
        });
        Button clear = new Button("C", click -> {
            display.setLabel(" ");
            display.setValue("0");
        });
        Button del = new Button("Del", click -> {
            if (display.getValue().length() == 1){
                display.setValue("0");
            } else {
                display.setValue((display.getValue()).substring(0, display.getValue().length()-1));
            }
        });
        row1.add(lBrac, clearEntered, clear, del);
        
        HorizontalLayout row2 = new HorizontalLayout();
        Button rBrac = new Button(")", click -> {
            updateCalc(display, ")");
        });
        Button squared = new Button("^", click -> {
            updateCalc(display, "^");
        });
        Button squareRoot = new Button("sqrt", click -> {
            display.setValue("sqrt(" + display.getValue() + ")");
        });
        Button divide = new Button("/", click -> {
            updateLabel(display, "/");
        });
        row2.add(rBrac, squared, squareRoot, divide);
        
        HorizontalLayout row3 = new HorizontalLayout();
        Button seven = new Button("7", click -> {
            updateCalc(display, "7");
        });
        Button eight = new Button("8", click -> {
            updateCalc(display, "8");
        });
        Button nine = new Button("9", click -> {
            updateCalc(display, "9");
        });
        Button multiply = new Button("x", click -> {
            updateLabel(display, "*");
        });
        row3.add(seven, eight, nine, multiply);
        
        HorizontalLayout row4 = new HorizontalLayout();
        Button four = new Button("4", click -> {
            updateCalc(display, "4");
        });
        Button five = new Button("5", click -> {
            updateCalc(display, "5");
        });
        Button six = new Button("6", click -> {
            updateCalc(display, "6");
        });
        Button minus = new Button("-", click -> {
            updateLabel(display, "-");
        });
        row4.add(four, five, six, minus);
        
        HorizontalLayout row5 = new HorizontalLayout();
        Button one = new Button("1", click -> {
            updateCalc(display, "1");
        });
        Button two = new Button("2", click -> {
            updateCalc(display, "2");
        });
        Button three = new Button("3", click -> {
            updateCalc(display, "3");
        });
        Button plus = new Button("+", click -> {
            updateLabel(display, "+");
        });
        row5.add(one, two, three, plus);
        
        HorizontalLayout row6 = new HorizontalLayout();
        Button plus_minus = new Button("+\\-", click -> {
            Double value = Double.parseDouble(display.getValue()) * -1;
            display.setValue(Double.toString(value));
        });
        Button zero = new Button("0", click -> {
            updateCalc(display, "0");
        });
        Button comma = new Button(",", click -> {
            updateCalc(display, ".");
        });
        Button equals = new Button("=", click -> {
            updateLabel(display, "");
            double ans = eval(display.getLabel());
            display.setValue("ans: " + Double.toString(ans));
            calcHisLayout.add(new Span(display.getLabel() + " = " + Double.toString(ans)));
        });
        row6.add(plus_minus, zero, comma, equals);

        VerticalLayout calcLayout = new VerticalLayout();
        calcLayout.add(display, row1, row2, row3, row4, row5, row6);
        calc.add(calcLayout);
        hisDetails.addContent(calcHisLayout);
        calcHistory.add(hisDetails);
        Page.add(calcDivs);
        calcDivs.add(calc, calcHistory);
    }

    private void timerFunc(Div Page){
        Page.setText("Timer");
    }

    private void calFunc(Div Page){
        Page.setText("Calender");
    }


    private Button createRemoveButton(Grid<Task> grid, Task item) {
        @SuppressWarnings("unchecked")
        Button button = new Button(new Icon(VaadinIcon.TRASH), clickEvent -> {
            ListDataProvider<Task> dataProvider = (ListDataProvider<Task>) grid.getDataProvider();
            dataProvider.getItems().remove(item);
            dataProvider.refreshAll();
        });
        button.addThemeVariants(ButtonVariant.LUMO_SMALL, ButtonVariant.LUMO_ICON, ButtonVariant.LUMO_TERTIARY);
        return button;
    }

    private Select<State> taskStatus(){
        Select<State> status = new Select<>();
        status.setItems(
            new State(VaadinIcon.HOURGLASS, "Pending"),
            new State(VaadinIcon.CHECK, "Done")
        );
        status.setPlaceholder("set status");
        status.getElement().setAttribute("theme", "small");
        status.addValueChangeListener(
            event -> status.setValue(event.getValue())
        );
        
        status.setRenderer(new ComponentRenderer<Component, State>(state -> {
            Div text = new Div();
            text.setText(state.getText());
            
            FlexLayout wrapper = new FlexLayout();
            text.getStyle().set("margin-left", "0.5em");
            wrapper.add(state.getIcon().create(), text);
            return wrapper;
        }));

        return status;
    }

    // Calculator operations
    public static double eval(final String str) {
        return new Object(){
            int pos = -1, ch;

            void nextChar() {
                ch = (++pos < str.length()) ? str.charAt(pos) : -1;
            }

            boolean eat(int charToEat){
                while (ch == ' ') nextChar();
                if (ch == charToEat){
                    nextChar();
                    return true;
                }
                return false;
            }

            double parse() {
                nextChar();
                double x = parseExpression();
                if (pos < str.length()) throw new RuntimeException("Unexpected: " + (char)ch);
                return x;
            }

            double parseExpression(){
                double x = parseTerm();
                for (;;) {
                    if (eat('+')) x += parseTerm();
                    else if (eat('+')) x -= parseTerm();
                    else return x;
                }
            }

            double parseTerm(){
                double x = parseFactor();
                for (;;){
                    if (eat('*')) x *= parseFactor();
                    else if (eat('/')) x /= parseFactor();
                    else return x;
                }
            }

            double parseFactor(){
                if (eat('+')) return parseFactor();
                if (eat('-')) return -parseFactor();

                double x;
                int startPos = this.pos;
                if (eat('(')) {
                    x = parseExpression();
                    eat(')');
                } else if ((ch >= '0' && ch <= '9') || ch == '.'){
                    while ((ch >= '0' && ch <= '9') || ch == '.') nextChar();
                    x = Double.parseDouble(str.substring(startPos, this.pos));
                } else if (ch >= 'a' && ch <= 'z'){
                    while (ch >= 'a' && ch <= 'z') nextChar();
                    String func = str.substring(startPos, this.pos);
                    x = parseFactor();
                    if (func.equals("sqrt")) x = Math.sqrt(x);
                    else if (func.equals("sin")) x = Math.sin(Math.toRadians(x));
                    else if (func.equals("cos")) x = Math.cos(Math.toRadians(x));
                    else if (func.equals("tan")) x = Math.tan(Math.toRadians(x));
                    else throw new RuntimeException("Unknown function: " + func);
                } else {
                    throw new RuntimeException("Unexpected: " + (char)ch);
                }

                if (eat('^')) x = Math.pow(x, parseFactor());

                return x;
            }
        }.parse();
    }

    private void updateCalc(TextField display, String val){
        if (display.getValue().equals("0")){
            display.setValue("");
        } else if (display.getValue().startsWith("ans: ")){
            display.setValue("");
            display.setLabel(" ");
        }
        display.setValue(display.getValue() + val);
    }

    private void updateLabel(TextField display, String opr){
        if (display.getValue().startsWith("ans: ")){
            display.setLabel(" ");
            display.setValue(display.getValue().substring(5));
        }
        display.setLabel(display.getLabel() + display.getValue() + opr);
        display.setValue("0");
    }
}
