/*
Factory method is a creational design pattern which solves the problem of creating 
product objects without specifying their concrete classes...

Dialog Rendering
This example illustrates how to organize a GUI framework into independent
modules using dynamic dispatch.
*/
mod gui;
mod html_gui;
mod init;
mod windows_gui;

use init::initialize;


fn main() {
    let dialog = initialize();
    dialog.render();
    dialog.refresh();
}