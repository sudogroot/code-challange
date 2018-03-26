import {Component, OnInit} from '@angular/core';
import {BookDetailService} from './book-detail.service';
import {finalize} from 'rxjs/operators';
import {BookDetail} from '@app/models/book-detail';
import {ActivatedRoute} from '@angular/router';
import {CookieService} from 'ngx-cookie-service';


@Component({
  selector: 'app-book-detail',
  templateUrl: './book-detail.component.html',
  styleUrls: ['./book-detail.component.scss']
})
export class BookDetailComponent implements OnInit {

  bookDetail: BookDetail;
  isLoading: boolean;
  isbn: string;
  cookieExists: boolean = this.cookieService.check('user_name');


  constructor(private bookDetailService: BookDetailService, private activeRouter: ActivatedRoute,
              private cookieService: CookieService) {
  }

  ngOnInit() {

    this.activeRouter.params.subscribe(params => {
      this.isbn = params['isbn'];
      this.getBookDetail(this.isbn);

    });
  }

  getBookDetail(isbn: string) {
    this.isLoading = true;
    this.bookDetailService.getBookDetail(isbn)
      .pipe(finalize(() => {
        this.isLoading = false;
      }))
      .subscribe((bookDetail: BookDetail) => {
        this.bookDetail = bookDetail;
      });
  }

  onComment(newComment: string) {
    // todo i could improve this
    this.bookDetailService.postComment(this.isbn, newComment).subscribe((bookDetail: BookDetail) => {
      this.getBookDetail(this.isbn);
    });
  }

  onStared(newStars: number) {
    // todo i could improve this
    this.bookDetailService.postStars(this.isbn, newStars).subscribe((bookDetail: BookDetail) => {
      this.getBookDetail(this.isbn);
    });
  }

}
