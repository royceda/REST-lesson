import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { AgmCoreModule } from '@agm/core';
import { HttpClientModule } from '@angular/common/http';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';

import { NgbModule } from '@ng-bootstrap/ng-bootstrap';
import { MapComponent } from './map/map.component';
import { TableComponent } from './table/table.component';


@NgModule({
  declarations: [
    AppComponent,
    MapComponent,
    TableComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    NgbModule,
    HttpClientModule,
    AgmCoreModule.forRoot({
      apiKey: 'AIzaSyBURM95bcFJd0qYA8BBrROv-ICalgLqg7Q'
    })
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
