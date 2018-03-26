import {Component, OnInit} from '@angular/core';
import {finalize} from 'rxjs/operators';

import {BooksService} from './books.service';
import {BookList} from '@app/models/book';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.scss']
})
export class HomeComponent implements OnInit {

  books: BookList;
  isLoading: boolean;

  constructor(private booksService: BooksService) {
  }

  ngOnInit() {
    this.getBooks();
  }

  getBooks(page: string = '') {
    this.isLoading = true;
    this.booksService.getBooksList(page)
      .pipe(finalize(() => {
        this.isLoading = false;
      }))
      .subscribe((books: BookList) => {
        this.books = books;
      });

  }


}
