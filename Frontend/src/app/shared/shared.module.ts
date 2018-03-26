import {NgModule} from '@angular/core';
import {CommonModule} from '@angular/common';
import {FlexLayoutModule} from '@angular/flex-layout';

import {MaterialModule} from '@app/material.module';
import {LoaderComponent} from './loader/loader.component';
import {BooksComponent} from './books/books.component';

@NgModule({
  imports: [
    FlexLayoutModule,
    MaterialModule,
    CommonModule
  ],
  declarations: [
    LoaderComponent,
    BooksComponent
  ],
  exports: [
    LoaderComponent,
    BooksComponent
  ]
})
export class SharedModule {
}
