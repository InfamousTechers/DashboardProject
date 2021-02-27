package com.dash.dashboard.scraper.java;

import com.dash.dashboard.views.dashboard.Gradebook;

import java.sql.Connection;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;
import java.util.ArrayList;
import java.util.List;

/**
 * @author brandonpahla
 * @email brandon.m.paahla@gmail.com
 */
public class GradebookTable extends ToolsTables {
    private Connection connection;

    public GradebookTable(){
        connection = super.connect();
    }

    public List<Gradebook> gradesList() {
        List<Gradebook> grades = new ArrayList<>(0);
        try {
            ResultSet rs = this.selectAll();
            // loop through the result set
            while (rs.next()) {
                grades.add(new Gradebook(rs.getString("Course"),
                        rs.getString("Title"),
                        rs.getString("Mark"),
                        rs.getString("Total")));
            }
        } catch (SQLException e) {
        }
        return grades;
    }

    @Override
    public ResultSet selectAll() {
        String sql = "SELECT Course, Title, Mark, Total  FROM Gradebook";
        ResultSet rs;
        try{
            Statement stmt  = this.connection.createStatement();
            rs    = stmt.executeQuery(sql);
            return rs;
        } catch (SQLException e) {
            System.out.println(e.getMessage());
        }
        return null;
    }

    @Override
    public void printAll() {
        ResultSet rs = this.selectAll();
        // loop through the result set
        try {
            while (rs.next()) {
                System.out.println(rs.getString("Course") + "\t" +
                        rs.getString("Title") + "\t" +
                        rs.getString("Mark") + "\t" +
                        rs.getString("Total"));
            }
        }catch (SQLException e){
            System.out.println(e.getMessage());
        }
    }
}
