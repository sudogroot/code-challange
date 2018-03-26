import {NgModule} from '@angular/core';
import {CommonModule} from '@angular/common';
import {TranslateModule} from '@ngx-translate/core';
import {FlexLayoutModule} from '@angular/flex-layout';

import {MaterialModule} from '@app/material.module';
import {BookDetailRoutingModule} from './book-detail-routing.module';
import {BookDetailComponent} from './book-detail.component';
import {StarsComponent} from './stars/stars.component';
import {CommentsComponent} from './comments/comments.component';
import {BookDetailService} from './book-detail.service';
import {FormsModule} from '@angular/forms';
import { SharedModule } from '@app/shared';


@NgModule({
  imports: [
    CommonModule,
    TranslateModule,
    FlexLayoutModule,
    MaterialModule,
    BookDetailRoutingModule,
    FormsModule,
    SharedModule
  ],
  declarations: [
    BookDetailComponent,
    CommentsComponent,
    StarsComponent
  ],
  providers: [
    BookDetailService
  ]
})
export class BookDetailModule {
}
